/**
 * Created by hamid on 3/12/16.
 */


$(document).ready(function(){

    $('#userPost_seeAll').click(function(){
        $('#userPost_all').css('display','block');
        $('#userPost_seeAll').css('display','none');
        $('#userPost_hideAll').css('display','block');
    });

    $('#userPost_hideAll').click(function(){
        $('#userPost_all').css('display','none');
        $('#userPost_hideAll').css('display','none');
        $('#userPost_seeAll').css('display','block');
    });


    $('.dropDown').click(function(event){
        var id=jQuery(this).attr('id');
        if($('#'+id+'_div').css('display')=='none'){
            $('#'+id+'_div').slideDown();
            $('#'+id+' div img').attr('src','/static/icons/actor/triangle_up.png');
        }
        else{
            $('#'+id+'_div').slideUp();
            $('#'+id+' div img').attr('src','/static/icons/actor/triangle_down.png');
        }
    });


});
