function portfolio(tab_img) {
    if(tab_img.length > 0){
        line = getLine(tab_img);
        setLine(line);
        portfolio(tab_img.slice(line.length,tab_img.length));
    }
}

function getLine(tab_img) {
    var i = 1,
    nb_max_img = false;
    while (!nb_max_img) {
        nb_max_img = testLine(tab_img.slice(0,i));
        if(tab_img.length < i){
            nb_max_img = true;
        }
        i++;
    }
    return(tab_img.slice(0,i-2));
}

function testLine(tab_img) {
    var total_width = getTotalWidth(tab_img);
    if (total_width > window.innerWidth) {
        return true;
    }
    return false;
}

function setLine(line) {
    var [min_ratio,fixed_height] = getMinRatioAndFixedHeight(line),
        total_width = 0;
    for (var i = 0; i < line.length; i++) {
        var own_ratio = line.eq(i).width() / line.eq(i).height();
        line.eq(i).width(fixed_height*own_ratio);
        total_width += line.eq(i).width();
    }

    var perfect_ratio = (window.innerWidth/total_width)*0.98;
    for (var i = 0; i < line.length; i++) {
        line.eq(i).width(line.eq(i).width()*perfect_ratio);
        line.eq(i).css('border','solid black 2px');
    }

}

function getTotalWidth(tab_img) {
    var [min_ratio,fixed_height] = getMinRatioAndFixedHeight(tab_img);
    var total_width = 0;
    for (var i = 0; i < tab_img.length; i++) {
        var own_ratio = tab_img.eq(i).width() / tab_img.eq(i).height();
        total_width += fixed_height * own_ratio;
    }
    return total_width;
}

function getMinRatioAndFixedHeight(tab_img){
    var min_ratio = Number.MAX_VALUE;
    for (var i = 0; i < tab_img.length; i++) {
        var width = tab_img.eq(i).width();
        var height = tab_img.eq(i).height();
        var ratio = width/height;
        if(ratio < min_ratio){
            min_ratio = ratio;
        }
    }
    // hauteur de l'image au plus petit ratio à min_width_img
    const fixed_height = min_width_img/min_ratio;
    return [min_ratio,fixed_height];
}

function timer(){
    setTimeout(portfolio(TAB_IMG),200);
}

const min_width_img = 200;
var TAB_IMG = $('.portfolio > li > img'),
    margin_width = 2;

$( document ).ready(portfolio(TAB_IMG));
$( window ).resize(timer);
