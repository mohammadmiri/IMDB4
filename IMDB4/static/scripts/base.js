

$(document).ready(function(){


    var sliderWidth=$('.movie_slider_images_image').width();
    var sliderHeight=$('.movie_slider_images_image').height()+6;
    var sliderCount=$('#movie_slider_images ul li').length;
    var sliderShowCount=4;


    var images=Array();
    var descriptions=Array();
    var celebrities=Array();



    $('#test_content_images').height(sliderShowCount*(sliderHeight+9));



    $('#image_test').mouseenter(function(){
        $('#panel_test').slideDown('slow');
    });

    $('#image_test').mouseleave(function(){
        $('#panel_test').slideUp('slow');
    });






    $('#movie_bestDialogue_seeAll').click(function(){
        $('#movie_bestDialogue_seeAll').hide();
        //document.getElementById('movie_bestDialogue').setAttribute(['overflow'],['auto']);
        $("#movie_bestDialogue_2").css('display','block');
    });


    $('#movie_bestDialogue_2_less').click(function(){
        $('#movie_bestDialogue_seeAll').show();
        $('#movie_bestDialogue_2').css('display','none');
    });


    $('#actor_userPost_seeAll').click(function(){
        $('#actor_userPost_all').css('display','block');
        $('#actor_userPost_seeAll').css('display','none');
        $('#actor_userPost_hideAll').css('display','block');
    });

    $('#actor_userPost_hideAll').click(function(){
        $('#actor_userPost_all').css('display','none');
        $('#actor_userPost_hideAll').css('display','none');
        $('#actor_userPost_seeAll').css('display','block');
    });


    $('.dropDown').click(function(event){
        var id=jQuery(this).attr('id');
        if($('#'+id+'_div').css('display')=='none'){
            $('#'+id+'_div').css('display','block');
        }
        else{
            $('#'+id+'_div').css('display','none');
        }
    });





    $('.signup_searchType').keyup(function(event){

        $.ajax({url:"http://localhost:8000/auth/search/",success:function(result){
            id=event.target.id;
            var parent=event.target.parentElement.parentElement;
            var add=parent.getElementsByClassName('signup_suggestion')[0];
            add.style.display='block';

            var child=add.firstChild;
            while(add.firstChild){
                add.removeChild(add.firstChild);
            }

            for(var i=0;i<Object.keys(result).length;i++){
                var div=document.createElement('div');
                div.innerHTML=result[i];
                div.className='signup_oneSuggestion';
                add.appendChild(div);
            }


        }})
    });




    $('.signup_suggestion').on('click', '.signup_oneSuggestion', function(event) {

        console.log(event.target.className);

        var string=event.target.innerHTML;
        var div=document.createElement("div");
        div.innerHTML='<p class="signup_element_text">'+string+'</p>';
        div.className+="signup_element";

        var close=document.createElement("div");
        close.className="signup_element_close";
        close.innerHTML='<button class="signup_element_close_btn" type="button">' +
        '<img src="/static/icons/signup/close.png" class="signup_element_close_btn_img"></button>';
        div.appendChild(close);

        var parent=event.target.parentElement.parentElement;
        var add=parent.getElementsByClassName('signup_addSuggestion')[0];
        //console.log('add: '+add.id+'  '+add.className);

        add.appendChild(div);
    });


    $('body').on('click','.signup_element_close_btn',function(event){

        var thisElement=event. target.parentElement.parentElement.parentElement;
        var parent=thisElement.parentElement;
        parent.removeChild(thisElement);

    });




    $('.signup_searchType').blur(function(event){

        setTimeout(function(){

            var parent=event.target.parentElement.parentElement;
            var add=parent.getElementsByClassName('signup_suggestion')[0];

            while(add.firstChild){
                add.removeChild(add.firstChild);
            }

        },200);

    });




    $('#signup_formButtons_submit').click(function(event){

        var dataForm=$('#signup_form');
        var inputType=dataForm.find('#signup_flavorMovie_inputText');
        //("signup_flavorMovie_inputText");

        var array=$('#signup_form').find('.signup_addSuggestion');
        for(var i=0;i<array.length;i++){
            var parent=array[i].parentElement;
            var inputType=$(parent).find('.signup_searchType');
            console.log(inputType[0].className);
            console.log('parent: '+parent.className);


            var elements=$(array[i]).find('.signup_element');
            var temp=$(elements[0]).find('p');
            var string=$(temp[0]).innerHTML;
            console.log('temp.innerHTML: '+$(temp).innerHTML);
            console.log('temp: '+$(temp).className);
            console.log('string: '+string);

            for(var j=1;j<elements.length;j++){
                string+='_'+$(elements[j]).find('p').innerHTML;
            }

            $(inputType[0]).val(string);
            console.log('val: '+$(inputType[0]).val());
        }

        console.log(inputType.val());

    });







    $('#movie_slider_images ul').css({height:sliderCount*sliderHeight});
    $('#movie_slider_images').css({height:sliderShowCount*sliderHeight});
    //$('#test_content_images').css({width:sliderWidth, height:sliderCount*sliderHeight});

    $('#movie_slider_arrowUp').click(function(){
        $('#movie_slider_images ul').animate({top:-sliderHeight} ,200, function () {
            $('#movie_slider_images ul li:first-child').appendTo('#movie_slider_images ul');
            $('#movie_slider_images ul').css('top', '');}
        );
    });


    $('#movie_slider_arrowDown').click(function(){
        $('#movie_slider_images ul').animate({top:sliderHeight}, 200, function () {
            $('#movie_slider_images ul li:last-child').prependTo('#movie_slider_images ul');
            $('#movie_slider_images ul').css('top', '');
        });
    });




    $('.movie_slider_images_button').click(function(event){

        var imageIndex=event.target.id;


        var parentElement=event.target.parentElement;
        var image=parentElement.innerHTML;

        var className=$('#movie_slider_mainImage div img').attr('class');
        var id=$('#movie_slider_mainImage div img').attr('id');

        $('#movie_slider_mainImage div').html('<img src='+images[imageIndex]+'>');
        $('#movie_slider_mainImage div img').attr('class',className);
        $('#movie_slider_mainImage div img').attr('id',id);

        $('.movie_slider_mainImage_topText').html(celebrities[imageIndex]);
        $('.movie_slider_mainImage_downText').html(descriptions[imageIndex]);
    });








    $('#test_content_images ul').css({height:sliderCount*sliderHeight});
    //$('#test_content_images').css({width:sliderWidth, height:sliderCount*sliderHeight});

    $('#test_content_arrowUp').click(function(){
        $('#test_content_images ul').animate({top:-sliderHeight} ,200, function () {
            $('#test_content_images ul li:first-child').appendTo('#test_content_images ul');
            $('#test_content_images ul').css('top', '');}
        );
    });


    $('#test_content_arrowDown').click(function(){
        $('#test_content_images ul').animate({top:sliderHeight}, 200, function () {
            $('#test_content_images ul li:last-child').prependTo('#test_content_images ul');
            $('#test_content_images ul').css('top', '');
        });
    });




    $('.test_content_images_button').click(function(event){

        var imageIndex=event.target.id;
        refresh_slider(imageIndex);

    });





    $('.movie_slider_close').click(function(event){
        var slider_background=$('#movie_slider_background');
        slider_background.css({display:'none'});
    });


    $('#movie_info_seeAll a').click(function(event){
        console.log('movie_info_seeAll a');
        var slider_background=$('#movie_slider_background');
        slider_background.css({display:'block'});
        refresh_slider(0);
    });


    function refresh_slider(imageIndex){

        console.log('refresh_slider');

        //var parentElement=event.target.parentElement;
        //var image=parentElement.innerHTML;

        var className=$('#test_content_mainImage div img').attr('class');
        var id=$('#test_content_mainImage div img').attr('id');

        $('#test_content_mainImage div').html('<img src='+images[imageIndex]+'>');
        $('#test_content_mainImage div img').attr('class',className);
        $('#test_content_mainImage div img').attr('id',id);

        $('.test_content_mainImage_topText').html(celebrities[imageIndex]);
        $('.test_content_mainImage_downText').html(descriptions[imageIndex]);

    }



    jQuery(window).load(function(){
        $.ajax({url:"/test_highQualitySlider/",success:function(result){
            images=result.image_urls;
            descriptions=result.descriptions;
            celebrities=result.celebrities;
        }});
    });


    jQuery(window).load(function(){
        $('#index_nav_articles_0').addClass("active");
        $('#index_nav_articles_0').addClass("in");
    });




















});