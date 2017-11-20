//dynamically refresh when a new face is added
$(document).ready(
    function($){
        window.num_of_faces = $("img.pics_faces").length;
        count();
    }
);
var times = 0;
function count() {
    if(times<40) {
        $.ajax({
                url:"/main/if_add_face/",
                type:"post",
                data:{
                    num_of_faces: num_of_faces,
                },
                success:function(data){
                    if(data==1){
                        window.location.reload();
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
        times = times + 1;
        setTimeout("count()", 2000);
    }
}
