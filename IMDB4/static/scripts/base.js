

$(document).ready(function(){



    $('#base_main_search_box').keyup(function () {
        var value=document.getElementById('base_main_search_box').value;
        $.ajax({url:'http://localhost:8000/home/base/search_suggestion/'+value,success:function(result){
            //removing last search suggestion.
            var addSuggestion=$('#main_searchSuggestion');
            var children=addSuggestion.children();
            for(var i=0;i<children.length;i++){
                addSuggestion.removeChild(children[i]);
            }
            //adding new search suggestion.
            var array=result.movie_names;
            for(var i=0;i<array.length;i++){
                var search_item=$('<div class="base_searchSuggestionItem">' +
                    '<img src="' + result.movie_images[i] + '" class="base_searchSuggestionItem_image">' +
                    '<div class="base_searchSuggestionItem_info">' +
                        '<p class="base_searchSuggestionItem_info_name">' +
                            '<a href="">' +
                                result.movie_names[i] +
                            '</a>' +
                            '(' +
                            result.movie_yearProduction[i] +
                            ')' +
                        '</p>' +
                        '<p class="base_searchSuggestionItem_info_description">' +
                            result.movie_descriptions[i] +
                        '</p>' +
                    '</div>' +
                '</div>');

                $(addSuggestion).html('<div class="base_searchSuggestionItem">' +
                    '<img src="' + result.movie_images[i] + '" class="base_searchSuggestionItem_image">' +
                    '<div class="base_searchSuggestionItem_info">' +
                        '<p class="base_searchSuggestionItem_info_name">' +
                            '<a href="">' +
                                result.movie_names[i] +
                            '</a>' +
                            '(' +
                            result.movie_yearProduction[i] +
                            ')' +
                        '</p>' +
                        '<p class="base_searchSuggestionItem_info_description">' +
                            result.movie_descriptions[i] +
                        '</p>' +
                    '</div>' +
                '</div>');
            }

            array=result.celeb_names;
            for(var i=0;i<array.length;i++){
                var search_item=document.createElement('div');
                $(search_item).html('<div class="base_searchSuggestionItem">' +
                    '<img src="' + result.movie_images[i] + '" class="base_searchSuggestionItem_image">' +
                    '<div class="base_searchSuggestionItem_info">' +
                        '<p class="base_searchSuggestionItem_info_name">' +
                            '<a href="">' +
                                result.movie_names[i] +
                            '</a>' +
                        '</p>' +
                        '<p class="base_searchSuggestionItem_info_description">' +
                            result.movie_descriptions[i] +
                        '</p>' +
                    '</div>' +
                '</div>');

                var temp=addSuggestion.innerHTML;
                temp+=search_item;
                $(addSuggestion).html(temp);
            }
            
            var more_div=document.createElement('div');
            $(more_div).html('<p id="base_searchSuggestion_more">' +
            'بیشتر' +
            '</p>');
            
        }});
        
    });






    $('#image_test').mouseenter(function(){
        $('#panel_test').slideDown('slow');
    });

    $('#image_test').mouseleave(function(){
        $('#panel_test').slideUp('slow');
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
        }});
    });




    $('.signup_suggestion').on('click', '.signup_oneSuggestion', function(event) {
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



























});