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
        total_width = 0,
        ratios = [];
    for (var i = 0; i < line.length; i++) {
        var own_ratio = parseFloat(line[i].getAttribute('width')) / parseFloat(line[i].getAttribute('height'));
        ratios[i] = own_ratio;
        line[i].setAttribute('width',fixed_height*own_ratio);
        total_width += parseFloat(line[i].getAttribute('width'));
    }
    var w = window.innerWidth;
    if(w < 991){ // ATTENTION PUTEUH PC POURRIS VS IPAD
        var perfect_ratio = w/total_width;
    }
    else {
        var perfect_ratio = (w-20)/total_width;
    }
    lineHolder[lineNumber] = [];
    lineHolder[lineNumber][0] = 0;
    lineHolder[lineNumber][1] = [];
    for (var i = 0; i < line.length; i++) {
        line[i].setAttribute('width',parseFloat(line[i].getAttribute('width'))*perfect_ratio - padding_value);
        line[i].setAttribute('height',parseFloat(line[i].getAttribute('width'))/ratios[i]);
        lineHolder[lineNumber][1].push(line[i]);
    }
    lineHolder[lineNumber][0] = parseFloat(line[0].getAttribute('height'));
    lineNumber++;
}

function getTotalWidth(tab_img) {
    var [min_ratio,fixed_height] = getMinRatioAndFixedHeight(tab_img);
    var total_width = 0;
    for (var i = 0; i < tab_img.length; i++) {
        var own_ratio = parseFloat(tab_img[i].getAttribute('width')) / parseFloat(tab_img[i].getAttribute('height'));
        total_width += fixed_height * own_ratio;
    }
    return total_width;
}

function getMinRatioAndFixedHeight(tab_img){
    var min_ratio = Number.MAX_VALUE;
    for (var i = 0; i < tab_img.length; i++) {
        var width = parseFloat(tab_img[i].getAttribute('width'));;
        var height = parseFloat(tab_img[i].getAttribute('height'));
        var ratio = width/height;
        if(ratio < min_ratio){
            min_ratio = ratio;
        }
    }
    // hauteur de l'image au plus petit ratio à min_width_img
    const fixed_height = min_width_img/min_ratio;
    return [min_ratio,fixed_height];
}

// function timer(){
//     setTimeout(portfolio(TAB_IMG),10000);
// }

function resizeTimer(d) {
    portfolio(TAB_IMG);
    lazyloading();
}

const min_width_img = 250;
var TAB_IMG = $('.portfolio > li > a > img'),
    resizable = true,
    scrollable = true,
    DATE = new Date(),
    lineHolder = [],
    portfolioHeight = 0,
    lineNumber = 0,
    lineDisplayed = 0,
    padding_value = 2*parseFloat(window.getComputedStyle(document.querySelector('.portfolio > li')).paddingLeft);

function lazyloading() {
    var displayableImg = $('.portfolio > li > a > img[data-src]').length;
    while(displayableImg != 0 && portfolioHeight < $(window).height() + $(window).scrollTop()){
        for (var i = 0; i < lineHolder[lineDisplayed][1].length; i++) {
            lineHolder[lineDisplayed][1][i].setAttribute('src',lineHolder[lineDisplayed][1][i].getAttribute('data-src'));
            lineHolder[lineDisplayed][1][i].addEventListener("load", function (event) {
                $(this).removeAttr('data-src');
                $(this).css({display:'block'});
                $(this).css({opacity:'1'});
            });
        }
        portfolioHeight += lineHolder[lineDisplayed][0];
        lineDisplayed++;
    }
}

$(document).scroll(function() {
    if($(window).scrollTop() + $(window).height() >= $(document).height() -20) {
        lazyloading();
    }
});

$(document).ready(function () {
    portfolio(TAB_IMG);
    lazyloading();
});

$( window ).resize(function () {
    // d = new Date();
    portfolio(TAB_IMG);
    lazyloading();
});
