/**
 * Created by mohammad on 4/20/16.
 */

$(document).ready(function(){
    
    
    $('.signup_searchType').keyup(function(event){
        var element=event.target;
        var value=element.value;
        $.ajax({url:"http://localhost:8000/user/search_celebrities/"+value,success:function(result){
            var id=element.id;
            var parent=event.target.parentElement.parentElement;
            var add=parent.getElementsByClassName('signup_suggestion')[0];
            add.style.display='block';
            var child=add.firstChild;
            while(add.firstChild){
                add.removeChild(add.firstChild);
            }
            for(var i=0;i<result.celebrities.length;i++){
                var div=document.createElement('div');
                div.innerHTML=result.celebrities[i].name;
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
        var thisElement=event.target;
        for(var i=0;i<3;i++) {
            if (thisElement.className != 'signup_element') {
                thisElement=thisElement.parentElement;
            }
        }
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
        var array=document.getElementsByClassName('signup_addSuggestion');
        for(var i=0;i<array.length;i++){
            var parent=array[i].parentElement;
            var inputType=parent.getElementsByClassName('signup_searchType');
            var elements=array[i].getElementsByClassName('signup_element');
            if(elements.length==0){
                continue;
            }
            var temp=elements[0].getElementsByTagName('p');
            var string=temp[0].innerHTML;
            for(var j=1;j<elements.length;j++){
                string+='_'+elements[j].getElementsByTagName('p')[0].innerHTML;
            }
            inputType[0].value=string;
        }
        var form=$('#signup_form').serializeArray();
        var url=form.action;
        $.ajax({
            type:'POST',
            url:url,
            data:form,
            success:function(){
                console.log('form has been sent successfully');
            }
        });


        // console.log('url: '+url);
        // $.post(url,form.dataset);
    });

});





