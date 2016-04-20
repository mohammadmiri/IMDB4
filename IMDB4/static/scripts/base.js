

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



});