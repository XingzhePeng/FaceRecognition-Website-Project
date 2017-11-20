from django.db import models


class Picture(models.Model):
    username = models.CharField(max_length=150)
    picname = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    is_detected = models.BooleanField(default=0)


class Face(models.Model):
    username = models.CharField(max_length=150)
    uid = models.CharField(max_length=150)
    show_pic = models.CharField(max_length=150)
    face_info = models.CharField(max_length=150)


class PicFace(models.Model):
    username = models.CharField(max_length=150)
    small_pic = models.CharField(max_length=150)
    source_pic = models.CharField(max_length=150)
    uid = models.CharField(max_length=150)
    is_identified = models.BooleanField(default=0)
