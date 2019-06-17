$('document').ready(($) => {
	
	/******* Nav scroll event **********/
	$(window).scroll(function() {
        var scrollTop = $(window).scrollTop();

        if (scrollTop === 0) {
			$('.navbar').removeClass('bg-white border-bottom-pink')
        } else {
        	$('.navbar').addClass('bg-white border-bottom-pink')
        }
    });

    $("a[href^='#']").click(function(e) {
		e.preventDefault();

		var position = $($(this).attr("href")).offset().top;
		
		$("body, html").animate({
			scrollTop: position
		}, 1000);
	});
});