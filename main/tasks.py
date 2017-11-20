from aip import AipFace
from .models import *
from PIL import Image
import os
import re
import time
from demo import celery_app
from django.conf import settings as django_settings

PIC_PATH = os.path.join(django_settings.BASE_DIR, 'PIC')

APP_ID = '10128403'
API_KEY = 'zeUnwI5xCIt2YLUasYNGKFpw'
SECRET_KEY = 'g1KnckhU4iMTumuOkwk4hYwWzwxhEkGL'
FACE_TRUST = 0.6
SAME_TRUST_1 = 61
SAME_TRUST_2 = 51

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


@celery_app.task()
def recog(username):
    detect(username)
    identify(username)
    return


@celery_app.task()
def re_identify_task(username):
    smallimgs = PicFace.objects.filter(username=username)
    if len(smallimgs)==0:
        return
    else:
        for smallimg in smallimgs:
            smallimg.is_identified=0
            smallimg.uid = re.sub('[^A-Za-z0-9]', '', smallimg.small_pic)
            smallimg.save()
        try:
            Face.objects.filter(username=username).delete()
            identify(username)
            group_users = aipFace.getGroupUsers(username)
            if group_users['result_num'] == 0:
                return
            results = group_users['result']
            for result in results:
                uid = result['uid']
                aipFace.deleteGroupUser(username, uid)
                time.sleep(2)
        except:
            return


def detect(username):
    detect_num = 0
    bigimgs = Picture.objects.filter(username=username, is_detected=0)
    while len(bigimgs) > 0 and detect_num < 2:
        for bigimg in bigimgs:
            detect = aipFace.detect(get_file_content(os.path.join(PIC_PATH, bigimg.picname)),
                                    {
                                        'max_face_num': 8,
                                        'face_fields': 'face_probability,landmark',
                                    }
                                    )
            if 'error_code' in detect:
                continue
            results = detect['result']
            for index, result in enumerate(results):
                if result['face_probability'] < FACE_TRUST:
                    continue
                x = []
                y = []
                landmark72 = result['landmark72']
                for landmark in landmark72:
                    x.append(landmark['x'])
                    y.append(landmark['y'])
                x_max = max(x)
                x_min = min(x)
                y_max = max(y)
                y_min = min(y)
                x_cha = x_max - x_min
                y_cha = y_max - y_min
                if x_cha >= y_cha:
                    x_fix = int(x_cha / 5)
                    y_fix = int(7 * x_cha / 10 - y_cha / 2)
                else:
                    y_fix = int(y_cha / 5)
                    x_fix = int(7 * y_cha / 10 - x_cha / 2)
                im = Image.open(os.path.join(PIC_PATH, bigimg.picname))
                region = im.crop((x_min - x_fix, y_min - y_fix, x_max + x_fix, y_max + y_fix))
                (shotname, extension) = os.path.splitext(bigimg.picname)
                small_pic_name = u'{0}_{1}{2}'.format(shotname, index, extension)
                region.save(os.path.join(PIC_PATH, small_pic_name))
                new_small = PicFace(username=username,
                                    small_pic=small_pic_name,
                                    source_pic=bigimg.picname,
                                    uid=re.sub('[^A-Za-z0-9]', '', small_pic_name),
                                    )
                new_small.save()
            bigimg.is_detected = 1
            bigimg.save()
        bigimgs = Picture.objects.filter(username=username, is_detected=0)
        detect_num += 1


def identify(username):
    identify_num = 0
    smalls = PicFace.objects.filter(username=username, is_identified=0)
    while len(smalls) > 0 and identify_num < 2:
        for small in smalls:
            face_num = len(Face.objects.filter(username=username))
            if face_num > 0:
                identifyUser = aipFace.identifyUser(
                    username,
                    get_file_content(os.path.join(PIC_PATH, small.small_pic)),
                    {
                        'user_top_num': 2,
                        'face_top_num': 1,
                    }
                )
                if 'error_code' in identifyUser:
                    continue
                first_face = identifyUser['result'][0]
                first_face_uid = first_face['uid']
                first_score = first_face['scores'][0]
                if identifyUser['result_num'] == 1:
                    if first_score > SAME_TRUST_1:
                        addUser = aipFace.addUser(
                            first_face_uid,
                            '',
                            username,
                            get_file_content(os.path.join(PIC_PATH, small.small_pic))
                        )
                        if 'error_code' in addUser:
                            continue
                        small.uid = first_face_uid
                        small.save()
                        time.sleep(2)
                    else:
                        addUser = aipFace.addUser(
                            small.uid,
                            '',
                            username,
                            get_file_content(os.path.join(PIC_PATH, small.small_pic))
                        )
                        if 'error_code' in addUser:
                            continue
                        new_face = Face(username=username,
                                        uid=small.uid,
                                        show_pic=small.small_pic,
                                        face_info='')
                        new_face.save()
                        time.sleep(2)
                else:
                    second_face = identifyUser['result'][1]
                    second_face_uid = second_face['uid']
                    second_score = second_face['scores'][0]
                    if first_score > SAME_TRUST_1 or (first_score > SAME_TRUST_2 and second_face_uid == first_face_uid):
                        addUser = aipFace.addUser(
                            first_face_uid,
                            '',
                            username,
                            get_file_content(os.path.join(PIC_PATH, small.small_pic))
                        )
                        if 'error_code' in addUser:
                            continue
                        small.uid = first_face_uid
                        small.save()
                        time.sleep(2)
                    else:
                        addUser = aipFace.addUser(
                            small.uid,
                            '',
                            username,
                            get_file_content(os.path.join(PIC_PATH, small.small_pic))
                        )
                        if 'error_code' in addUser:
                            continue
                        new_face = Face(username=username,
                                        uid=small.uid,
                                        show_pic=small.small_pic,
                                        face_info='')
                        new_face.save()
                        time.sleep(2)




            else:
                addUser = aipFace.addUser(
                    small.uid,
                    '',
                    username,
                    get_file_content(os.path.join(PIC_PATH, small.small_pic))
                )
                if 'error_code' in addUser:
                    continue
                new_face = Face(username=username,
                                uid=small.uid,
                                show_pic=small.small_pic,
                                face_info='')
                new_face.save()
                time.sleep(2)
            small.is_identified = 1
            small.save()
        identify_num += 1
        smalls = PicFace.objects.filter(username=username, is_identified=0)
