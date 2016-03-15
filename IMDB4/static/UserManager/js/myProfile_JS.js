
jQuery(document).ready(function($){

    console.log('in rated right arrow click'+wrapperWidth_rated)

    // the properties listed below related to rated slide bar
    var itemCount_rated = $('#slideBar_rated_content_wrapper div').length;
    var itemWidth_rated = $('#slideBar_rated_content_wrapper div').width();
    var itemHeight_rated = $('#slideBar_rated_content_wrapper div').height();
    var wrapperWidth_rated = itemCount_rated * itemWidth_rated;

    console.log('in rated right arrow click'+wrapperWidth_rated)
	$('#slideBar_rated_content_wrapper').css({ width: wrapperWidth_rated });

    $('#rated.right_arrow').click(function() {
        console.log('in rated right arrow click'+wrapperWidth_rated)
        moveLeft('#slideBar_rated_content_wrapper', '#slideBar_rated_content_wrapper div', itemWidth_rated, 200, itemCount_rated)
    });

    $('#rated.left_arrow').click(function() {
        console.log('in rated left arrow click'+wrapperWidth_rated)
        moveRight('#slideBar_rated_content_wrapper', '#slideBar_rated_content_wrapper div', itemWidth_rated, 200, itemCount_rated)
    });



    // the properties listed below related to visited movies slide bar
    var itemCount_visited = $('#slideBar_rated_content_wrapper').length;
    var itemWidth_visited = $('#slideBar_rated_content_wrapper div').width();
    var itemHeight_visited = $('#slideBar_rated_content_wrapper div').height();
    var wrapperWidth_visited = itemCount_rated * itemWidth_rated;

	$('#slider ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });

    // the properties listed below related to last lists created by user slide bar
    var itemCount_listed = $('#slideBar_rated_content_wrapper').length;
    var itemWidth_listed = $('#slideBar_rated_content_wrapper div').width();
    var itemHeight_listed = $('#slideBar_rated_content_wrapper div').height();
    var wrapperWidth_listed = itemCount_rated * itemWidth_rated;

	$('#slider ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });





    function moveLeft(selectorOfWrapper, selectorOfItem, ItemWidth, duration, itemCount){
        if ( itemCount > 5) {
            $(selectorOfWrapper).animate({
                left: +ItemWidth
            }, duration, function () {
                $(selectorOfItem).prependTo(selectorOfWrapper);
                $(selectorOfWrapper).css('left', '');
            });
        }
    };

    function moveRight(selectorOfWrapper, selectorOfItem, ItemWidth, duration, itemCount){
        if(itemCount > 5) {
            $(selectorOfWrapper).animate({
                left: -ItemWidth
            }, duration, function () {
                $(selectorOfItem).appendTo(selectorOfWrapper);
                $(selectorOfWrapper).css('left', '');
            });
        }
    };

})





