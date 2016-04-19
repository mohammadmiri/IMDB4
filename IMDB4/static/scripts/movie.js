/**
 * Created by hamid on 3/12/16.
 */


$(document).ready(function () {

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
        var imageIndex=$(event.target).children()[0].id;
        var parentElement=event.target.parentElement;
        var image=parentElement.innerHTML;
        var className=$('#slider_mainImage div img').attr('class');
        var id=$('#slider_mainImage div img').attr('id');
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

    $('#info_seeAll a').click(function(event){
        console.log('movie_info_seeAll a');
        var slider_background=$('#slider_background');
        slider_background.css({display:'block'});
        var slider_background_dark=$('#slider_background_dark');
        slider_background_dark.css({display:'block'});
        // refresh_slider(0);
    });



    $('#bestDialogue_seeAll').click(function(){
        $('#bestDialogue_seeAll').hide();
        $('#bestDialogue_2').slideDown();
    });


    $('#bestDialogue_2_less').click(function(){
        $('#bestDialogue_seeAll').show();
        $('#bestDialogue_2').slideUp();
    });




    /**
     * loads data of slider.
     */
    jQuery(window).load(function(){
        console.log('finish');
        $.ajax({url:"/highQualitySlider/",success:function(result){
            console.log('success');
            console.log(result.image_urls);
            console.log(result.descriptions);
            console.log(result.celebrities);
            images=result.image_urls;
            descriptions=result.descriptions;
            celebrities=result.celebrities;
        }});
    });

});






