/**
 * Created by hamid on 3/12/16.
 */


$(document).ready(function(){
    
    var images=Array();
    var descriptions=Array();
    var celebrities=Array();

    var sliderWidth=$('.slider_images_image').width();
    var sliderHeight=$('.slider_images_image').height()+3;
    var sliderCount=$('#slider_images ul li').length;
    var sliderShowCount=4;

    $('#slider_images ul').css({height:sliderCount*sliderHeight});
    $('#slider_images').css({height:sliderShowCount*sliderHeight});

    
    
    $('#slider_arrowUp').click(function(){
        $('#slider_images ul').animate({top:-sliderHeight} ,200, function () {
            $('#slider_images ul li:first-child').appendTo('#slider_images ul');
            $('#slider_images ul').css('top', '');}
        );
    });

    $('#slider_arrowDown').click(function(){
        $('#slider_images ul').animate({top:sliderHeight}, 200, function () {
            $('#slider_images ul li:last-child').prependTo('#slider_images ul');
            $('#slider_images ul').css('top', '');
        });
    });

    $('.slider_images_button').click(function(event){
        var imageIndex=event.target.id;
        var parentElement=event.target.parentElement;
        // var image=parentElement.innerHTML;
        var className=$('#slider_mainImage div img').attr('class');
        var id=$('#slider_mainImage div img').attr('id');
        console.log(images[imageIndex]);
        $('#slider_mainImage div').html('<img src='+images[imageIndex]+'>');
        $('#slider_mainImage div img').attr('class',className);
        $('#slider_mainImage div img').attr('id',id);
        $('.slider_mainImage_topText').html(celebrities[imageIndex]);
        $('.slider_mainImage_downText').html(descriptions[imageIndex]);
    });

    $('.slider_close').click(function(event){
        var slider_background=$('#slider_background');
        slider_background.css({display:'none'});
        var slider_background_dark=$('#slider_background_dark');
        slider_background_dark.css({display:'none'});
    });
    

    $('#info_images_seeAll').click(function(event){
        var slider_background=$('#slider_background');
        slider_background.css({display:'block'});
        var slider_background_dark=$('#slider_background_dark');
        slider_background_dark.css({display:'block'});
        // refresh_slider(0);
    });
    
    
    
    
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



    $('.play_movie').click(function(event){
        console.log(play_movie_innerHTML);
        $('#frame_movie_background_dark').css({'display':'block'});
        $('.frame_movie_wrapper').css({'display':'block'});
        $('#play_movie_frame div').html(play_movie_innerHTML);
    });


    $('.exit_play_movie').click(function(){
        $('#play_movie_frame div').html('');
        $('#frame_movie_background_dark').css({'display':'none'});
        $('.frame_movie_wrapper').css({'display':'none'});
    });


    
    
    /**
     * loads data of slider.
     */
    jQuery(window).load(function(){
        var array=$('.images_url_hidden');
        for(var i=0;i<array.length;i++){
            images[i]=$(array[i]).html();
        }
        array=$('.images_description_hidden');
        for(var i=0;i<array.length;i++){
            descriptions[i]=$(array[i]).html();
        }
        array=$('.images_name_hidden');
        for(var i=0;i<array.length;i++){
            celebrities[i]=$(array[i]).html();
        }
    });


    /**
     * remove play movie inner html from its div permanently.
     * this code must be added to its div when user clicks on play video button.
     */
    jQuery(window).load(function(){
        var movie_element=$('.frame_movie_wrapper div')[0];
        play_movie_innerHTML=$(movie_element).html();
        $(movie_element).html('');
    });






});
