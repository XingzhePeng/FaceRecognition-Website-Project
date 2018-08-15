$(document).ready(
function($){
    var width = $("img.big_pic").width();
    var height = $("img.big_pic").height();
    if(height*1290 < width*814){
        $("img.big_pic").width(1290 + "px");
    }
    else{
        $("img.big_pic").height(814 + "px");
    }
});

function bigimg(obj) {
    var zoom = parseInt(obj.style.zoom)||100;
    zoom += event.wheelDelta/12;
    if (zoom > 0) {
        obj.style.zoom = zoom+"%";
        console.log(obj.style.zoom);
    }
    return false;
}