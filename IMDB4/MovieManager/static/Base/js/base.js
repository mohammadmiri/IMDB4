




$(document).ready(function(){
   $('#image_test').mouseenter(function(){
       $('#panel_test').slideDown('slow');
   });

   $('#image_test').mouseleave(function(){
       $('#panel_test').slideUp('slow');
   })






    $('#movie_bestDialogue_seeAll').click(function(){
        $('#movie_bestDialogue_seeAll').hide();
        //document.getElementById('movie_bestDialogue').setAttribute(['overflow'],['auto']);
        $("#movie_bestDialogue_2").css('display','block');
    });


    $('#movie_bestDialogue_2_less').click(function(){
        $('#movie_bestDialogue_seeAll').show();
        $('#movie_bestDialogue_2').css('display','none');
    })


    $('#actor_userPost_seeAll').click(function(){
        $('#actor_userPost_all').css('display','block');
        $('#actor_userPost_seeAll').css('display','none');
        $('#actor_userPost_hideAll').css('display','block');
    })

    $('#actor_userPost_hideAll').click(function(){
        $('#actor_userPost_all').css('display','none');
        $('#actor_userPost_hideAll').css('display','none');
        $('#actor_userPost_seeAll').css('display','block');
    })


    $('.dropDown').click(function(event){
        var id=jQuery(this).attr('id');
        console.log('#'+id+'_div');
        if($('#'+id+'_div').css('display')=='none'){
            $('#'+id+'_div').css('display','block');
        }
        else{
            $('#'+id+'_div').css('display','none');
        }
    })





});