
var months=new Array(31,31,31,31,31,31,30,30,30,30,30,29);
var monthNames=new Array("فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند")
var counter=0;
var created=0;

var delay = ( function() {
    var timer = 0;
    return function(callback, ms) {
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    };
})();


function change_date(){
    div=document.getElementById("signup_changeDate");
    if(div.style.display=='none') {
        counter = 0;
        div.style.display = 'block';
        document.getElementById("signup_changeDate_year").value="سال";
        if(created==0) {
            created=1;
            create_days();
        }
    }
    else{
        div.style.display='none';
    }
}




function create_days(){
    divDay=document.getElementById("signup_changeDate_days");
    for(var i=1;i<=31;i++){
        var div = document.createElement("div");
        div.innerHTML = i;
        div.id="signup_changeDate_numbers_"+i;
        div.className += "signup_changeDate_numbers";
        div.onclick = select_date;
        divDay.appendChild(div);
    }
}




function month_left(){
    counter--;
    if(counter==-1){
        counter=months.length-1;
    }
    refresh_date();
}





function month_right(){
    counter++;
    if(counter==months.length){
        counter=0;
    }
    refresh_date();
}




function refresh_date(){
    var month = document.getElementById("signup_changeDate_month");
    p = month.getElementsByTagName("p");
    p[0].innerHTML = monthNames[counter];
    $(".signup_changeDate_numbers").fadeOut("fast");
    number = months[counter];
    for (var i = 1; i <= number; i++) {
        $("#signup_changeDate_numbers_"+i).fadeIn("fast");
    }
    $(".signup_changeDate_number").fadeIn("fast");
}




function select_date(){
    console.log('select');
    document.getElementById("signup_birthday_day").value=this.innerHTML;
    document.getElementById("signup_birthday_month").value=counter+1;
    document.getElementById("signup_birthday_year").value=document.getElementById("signup_changeDate_year").value;

}







