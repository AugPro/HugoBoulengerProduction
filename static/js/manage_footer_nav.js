function manage_footer_nav() {
    if($(document).height() - ($(window).scrollTop() + $(window).height()) < Math.abs(20) ){
        $('.footer').show();
    } else {
        $('.footer').hide();
    }

    var w = window.innerWidth;
    if(w < 767){

    }
    else {
        if($(window).scrollTop() < 10){
            $('nav').unbind();
            $('nav').slideDown();
        } else {
            $('nav').unbind();
            $('nav').slideUp(100);
        }
    }
}

$( document ).ready(manage_footer_nav);
$( window ).resize(manage_footer_nav);
$( document ).scroll(manage_footer_nav);
