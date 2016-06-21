/**
 * Created by hamid on 6/21/2016.
 */

$(document).ready(function(){

    $('#add_item_input').keyup(function(){
        var listType=$('input[name=list_type]:checked').val();
        var value=$('#add_item_input').val();
        var addSuggestion=$('#search_suggestion');
        addSuggestion.html('');

        if(listType=='artist'){
            $.ajax({url:'http://localhost:8000/home/base/search_suggestion/'+value,success:function (result) {
                names=result['name_celebrity'];
                for(var i=0;i<names.length;i++) {
                    var wrapper = document.createElement('div');
                    wrapper.className='search_item';
                    var pTag = document.createElement('p');
                    pTag.innerHTML=names[i];
                    wrapper.appendChild(pTag);
                    addSuggestion.append(wrapper);
                }
            }});
        }

        if(listType=='movie'){
            $.ajax({url:'http://localhost:8000/home/base/search_suggestion/'+value,success:function(result){
                names=result['name_movie'];
                for(var i=0;i<names.length;i++) {
                    var wrapper = document.createElement('div');
                    wrapper.className='search_item';
                    var pTag = document.createElement('p');
                    pTag.innerHTML=names[i];
                    wrapper.appendChild(pTag);
                    addSuggestion.append(wrapper);
                }
            }});
        }
    });



    $('#add_item_input').blur(function(){
        var addSuggestion = $('#search_suggestion');
        setTimeout(function() {
            addSuggestion.html('');
        },100);
    });
    
    

    $('body').on('click','.search_item',function(event){
        var value=event.target.innerHTML;
        var addItem=$('#add_item div')[0];
        var wrapper=document.createElement('p');
        var button=document.createElement('button');
        button.type='button';
        button.className='close_button';
        var div=document.createElement('div');
        var img=document.createElement('img');
        img.src='/static/icons/close.png';
        div.appendChild(img);
        button.appendChild(div);
        wrapper.innerHTML=value;
        wrapper.appendChild(button);
        $(addItem).append(wrapper);
    });
    

    $('body').on('click','.close_button',function(event){
        var top=event.target;
        for(;;){
            if(top.className=='close_button'){
                break;
            }
            top=top.parentElement;
        }
        var deleteItem=top.parentElement;
        var wrapper=deleteItem.parentElement;
        wrapper.removeChild(deleteItem);
    });
    
});







