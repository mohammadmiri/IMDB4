
$(document).ready(function(){

    textes = $('.polling_optionWrapper p');

    var max=0;
    for(var i=0;i<$(textes).length;i++){
        if(max < $(textes[i]).height()){
            max = $(textes[i]).height();
        }
    }

    console.log('max: '+max)

    for (var i=0;i<textes.length;i++){
        $(textes[i]).css('height', max)
    }

});




