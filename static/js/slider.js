$(document).ready(function() {
	$(function(){
		var $i = 0,
		$slide = $('.slider div'),
		$IndexImg = $slide.length -1 ,
		$Timeout = 0;
		$slide.eq(0).css({opacity:1})

	  function slide(){
	 $TimeOut = setTimeout(function(){
		  if ( $i < $IndexImg ){
		  $i += 1 ;
		  } else {
		  $i = 0 ;
		  }
	  $nextSlide = $slide.eq($i);
	  $slide.eq($i-1).css({opacity:0})
	  $nextSlide.css({opacity:1});
	  slide();
	  },3000);
	  }
  slide();
  });
});
