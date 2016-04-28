

$(document).ready(function(){

    var mostVisited_names=Array();
    var index;
    var max_index;
    var mostVisited_ids=Array();



    var array=$('#sideBar_mostVisited_names_hidden p');
    for(var i=0;i<array.length;i++){
        mostVisited_ids[i]=$(array[i]).attr('id');
    }







    $('#base_main_search_box').keyup(function () {
        console.log('search box');
        var value=document.getElementById('base_main_search_box').value;
        $.ajax({url:'http://localhost:8000/home/base/search_suggestion/'+value,success:function(result){
            console.log(result);
            console.log(result.movie_descriptions);

            //removing last search suggestion.
            var addSuggestion=$('#main_searchSuggestion');
            var children=$(addSuggestion).children();
            for(var i=0;i<children.length;i++){
                addSuggestion.html('');
            }


            var movies_name=result['name_movie'];
            var movies_id=result['id_movie'];
            var movies_image=result['poster_movie'];
            var movies_year=result['year_movie'];
            var movies_director=result['director_movie'];

            var celebrities_image=result['picture_celebrity'];
            var celebrities_id=result['id_celebrity'];
            var celebrities_name=result['name_celebrity'];
            var celebrities_profession=result['profession_celerity'];



            for(var i=0;i<movies_name.length;i++){
                var movieWrapper=document.createElement('div');
                var movieInfoWrapper=document.createElement('div');
                var movieLink=document.createElement('a');
                var movieName=document.createElement('p');
                var movieDescription=document.createElement('p');
                var movieImage=document.createElement('img');

                movieLink.className='searchSuggestion_name';
                movieDescription.className='searchSuggestion_description';
                movieImage.className='searchSuggestion_image';

                movieLink.href='http://localhost:8000/movie/show/'+movies_id[i]+'/';
                movieName.innerHTML=movies_name[i]+' ('+movies_year[i]+')';
                movieDescription.innerHTML=movies_director[i];
                movieImage.src=movies_image[i];

                movieLink.appendChild(movieName);
                movieInfoWrapper.appendChild(movieLink);
                movieInfoWrapper.appendChild(movieDescription);
                movieWrapper.appendChild(movieImage);
                movieWrapper.appendChild(movieInfoWrapper);

                $(addSuggestion).append(movieWrapper);
            }

            for(var i=0;i<celebrities_name.length;i++){
                var celebWrapper=document.createElement('div');
                var celebInfoWrapper=document.createElement('div');
                var celebLink=document.createElement('a');
                var celebName=document.createElement('p');
                var celebDescription=document.createElement('p');
                var celebImage=document.createElement('img');

                celebLink.className='searchSuggestion_name';
                celebDescription.className='searchSuggestion_description';
                celebImage.className='searchSuggestion_image';

                celebLink.href='http://localhost:8000/celebrity/show/'+celebrities_id[i]+'/';
                celebName.innerHTML=celebrities_name[i];
                console.log(celebrities_profession.length);
                celebDescription.innerHTML=celebrities_profession[i];
                celebImage.src=celebrities_image[i];

                celebLink.appendChild(celebName);
                celebInfoWrapper.appendChild(celebLink);
                celebInfoWrapper.appendChild(celebDescription);
                celebWrapper.appendChild(celebImage);
                celebWrapper.appendChild(celebInfoWrapper);

                $(addSuggestion).append(celebWrapper);
            }

            var moreWrapper=document.createElement('div');
            var moreLink=document.createElement('a');
            var moreText=document.createElement('p');

            moreWrapper.className='searchSuggestion_more';

            moreLink.href='';
            moreText.innerHTML='بیشتر';

            moreLink.appendChild(moreText);
            moreWrapper.appendChild(moreLink);

            $(addSuggestion).append(moreWrapper);
        }});
    });


    $('#base_main_search_box').blur(function(){
        var addSuggestion=$('#main_searchSuggestion');
        var children=addSuggestion.children();
        setTimeout(function(){
            addSuggestion.html('');
        },100);
    });



    $('#mostVisited_arrowRight').click(function(){
        console.log('right');
        var slider_move=$('#sideBar_mostVisited_images div');
        var sliderWidth=$('#sideBar_mostVisited_images div img').width();
        $(slider_move).animate({right:-sliderWidth},200, function () {
            var first_child=$(slider_move).children('img:first-child');
            $(first_child).appendTo(slider_move);
            $(slider_move).css('right','');
        });

        index++;
        if(index==max_index+1){
            index=1;
        }
        $('#sideBar_mostVisited_control div p').html(index);
        $('#sideBar_mostVisited_control a p').html(mostVisited_names[index-1]);
        $('#sideBar_mostVisited_control a').attr('href','http://localhost:8000/movie/show/'+mostVisited_ids[index-1]+'/');

    });

    $('#mostVisited_arrowLeft').click(function(){
        console.log('left');
        var slider_move=$('#sideBar_mostVisited_images div');
        var sliderWidth=$('#sideBar_mostVisited_images div img').width();

        $(slider_move).animate({right:sliderWidth},200, function () {
            var last_child=$(slider_move).children('img:last-child');
            $(last_child).prependTo(slider_move);
            $(slider_move).css('right','');
        });

        index=index-1;
        if(index==0){
            index=max_index;
        }
        $('#sideBar_mostVisited_control div p').html(index);
        $('#sideBar_mostVisited_control a p').html(mostVisited_names[index-1]);
        $('#sideBar_mostVisited_control a').attr('href','http://localhost:8000/movie/show/'+mostVisited_ids[index-1]+'/');



    });




    jQuery(window).ready(function(){
        console.log('finish');
        var array=$('#sideBar_mostVisited_names_hidden p');
        for(var i=0;i<array.length;i++){
            mostVisited_names[i]=$(array[i]).html();
        }
        index=1;
        max_index=array.length;
    });













});