function menuUpdate() {
    var w = window.innerWidth;
    if(w < 767){
        if(!$('.menu-toggler').length){
            $('<div class="slide-img nav-img" style="background:url(img/logo.png) center center / contain no-repeat"></div>').insertAfter($('nav'));
            $('<div class="menu-toggler glyphicon glyphicon-home"></div>').insertAfter($('nav'));
        }
        $('.menu-toggler').unbind();
        $('.menu-toggler').click(function(){
            $('nav').slideToggle();
        });
    }
    else {
        $('.menu-toggler').unbind();
        $('.menu-toggler').remove();
        $('.slide-img').remove();
        $('nav').show();
    }
}

$( document ).ready(menuUpdate);
$( window ).resize(menuUpdate);
