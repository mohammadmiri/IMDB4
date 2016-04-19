/**
 * Created by hamid on 3/12/16.
 */



$(document).ready(function(){
    
    
    $('.play_movie').click(function(event){
        $('#frame_movie_background_dark').css({'display':'block'});
        var element=event.target;
        if(element.className!='play_movie'){
            element=element.parentElement;
        }
        var id=element.id;
        id=id+'_div';
        $('#'+id).css({'display':'block'});
    });


    $('.exit_play_movie').click(function(){
        $('#frame_movie_background_dark').css({'display':'none'});
        $('.frame_movie_wrapper').css({'display':'none'});
    });

    jQuery(window).load(function(){
        $('#nav_articles_0').addClass("active");
        $('#nav_articles_0').addClass("in");
        
    });
    
    

});