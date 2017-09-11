function menuUpdate() {
    var w = window.innerWidth;
    if(w < 767){
        if(!$('.responsive-plus').length){
            $('<span class="glyphicon glyphicon-plus responsive-plus"></span>').insertBefore($('.wrap > .sub-menu'));
            $('nav > ul > li').last().find('.responsive-plus').remove();
            $('.wrap').unbind();
            $('.wrap').click(function(){
                $(this).find('.sub-menu').slideToggle();
            });
        }
    }
    else {
        $('.responsive-plus').remove();
        $('.wrap').unbind();
        $('.wrap').find('.sub-menu').hide();
        $('.wrap').hover(function(){
            $(this).find('.sub-menu').stop(true,true).fadeIn(100);
        }, function(){
            $(this).find('.sub-menu').stop(true,true).fadeOut(100);
        });
    }
}

$( document ).ready(menuUpdate);
$( window ).resize(menuUpdate);
