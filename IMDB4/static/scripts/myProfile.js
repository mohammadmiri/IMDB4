/**
 * Created by hamid on 3/10/16.
 */


$(document).ready(function(){

    var sliderVerticalHeight=$('.sliderVertical_item').height()+1;
    var sliderVerticalShowCount=3;
    $('.sliderVertical_div').css({height:sliderVerticalShowCount*sliderVerticalHeight});


    var sliderWidth=$('.sliderMovie_div div div a img').width()+4;
    var sliderShowCount=5;
    $('.sliderMovie_div').css({width:sliderShowCount*sliderWidth});

    $('.slider_rightArrow').click(function(event){
        var parent=event.target.parentElement;
        var slider_move=$(parent).find('.sliderMovie_move')[0];
        var sliderWidth=$('.sliderMovie_move div').width();

        $(slider_move).animate({right:-sliderWidth},200, function () {
            var first_child=$(slider_move).find('div:first-child');
            $(first_child).appendTo(slider_move);
            $(slider_move).css('right','');
        });
    });

    $('.slider_leftArrow').click(function(event){
        var parent=event.target.parentElement;
        var slider_move=$(parent).find('.sliderMovie_move')[0];
        var sliderWidth=$('.sliderMovie_move div').width();

        $(slider_move).animate({right:sliderWidth},200, function () {
            var last_child=$(slider_move).children('div:last-child');
            $(last_child).prependTo(slider_move);
            $(slider_move).css('right','');
        });
    });



    $('.sliderVertical_topArrow').click(function(event){
        console.log('top arrow');
        var parent=event.target.parentElement;
        var slider_move=$(parent).find('.sliderVertical_move')[0];
        var sliderHeight=$('.sliderVertical_item').height();


        $(slider_move).animate({top:-sliderHeight},200,function(){
            var first_child=$(slider_move).children('div:first-child');
            console.log(first_child);
            console.log('after');
            $(first_child).appendTo(slider_move);
            $(slider_move).css('top','');
        });
    });

    $('.sliderVertical_bottomArrow').click(function(event){
        console.log('bottom arrow');
        var parent=event.target.parentElement;
        var slider_move=$(parent).find('.sliderVertical_move')[0];
        var sliderHeight=$('.sliderVertical_item').height();

        $(slider_move).animate({top:sliderHeight},200,function(){
            var last_child=$(slider_move).children('div:last-child');
            $(last_child).prependTo(slider_move);
            $(slider_move).css('top','');
        });
    });



});





















