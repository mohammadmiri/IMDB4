/**
 * Created by hamid on 4/7/16.
 */


$(document).ready(function(){

    $('.table_redBox_selectYear button').click(function(event){
        $('.selectYear_all').css({display:'none'});
        var element=event.target;
        var parent=element.parentElement;
        if(parent.tagName=='BUTTON'){
            parent=parent.parentElement;
        }
        var div=$(parent).children('.selectYear_all');
        $(div).css({display:'block'});
    });

    $('.table_redBox_selectYear button').blur(function(){
        setTimeout(function() {
                $('.selectYear_all').css({display: 'none'});
            }
        ,100);
    });

    $('.year_item').click(function(event){
        var element=event.target;
        if(element.tagName=='P'){
            var selectedYear=element.innerHTML;
            var parent=element.parentElement.parentElement.parentElement.parentElement;
            var year_div=parent.getElementsByClassName('year')[0];
            year_div=year_div.getElementsByTagName('p')[0];
            year_div.innerHTML=selectedYear;
        }
    });

});














