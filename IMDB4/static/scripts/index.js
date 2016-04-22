/**
 * Created by hamid on 3/12/16.
 */



$(document).ready(function(){

    var ids=Array();
    var movie_innerHTML=Array();
    
    
    $('.play_movie').click(function(event){
        $('#frame_movie_background_dark').css({'display':'block'});
        var element=event.target;
        if(element.className!='play_movie'){
            element=element.parentElement;
        }
        var id=element.id;
        id=id+'_div';
        var index=0;
        for(;index<ids.length;index++){
            if(id==ids[index]){
                break;
            }
        }
        $('#'+id+' div').html(movie_innerHTML[index]);
        $('#'+id).css({'display':'block'});
        
    });


    $('.exit_play_movie').click(function(event){
        var close=event.target;
        if(close.tagName!='button'){
            close=close.parentElement;
        }
        var parent=close.parentElement;
        var div=$(parent).children('div');
        $(div).html('');
        $('#frame_movie_background_dark').css({'display':'none'});
        $('.frame_movie_wrapper').css({'display':'none'});
    });

    jQuery(window).load(function(){
        $('#nav_articles_0').addClass("active");
        $('#nav_articles_0').addClass("in");

        var movie_elements=$('.frame_movie_wrapper');
        for(var i=0;i<movie_elements.length;i++){
            ids[i]=movie_elements[i].id;
            var temp=movie_elements[i].getElementsByTagName('div');
            movie_innerHTML[i]=temp[0].innerHTML;
            temp[0].innerHTML='';
        }
    });
    
    



















});