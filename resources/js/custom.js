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

	$('.navbar a').on('click', function() {
    	$('.navbar-toggler').click();
	});

    $("a[href^='#']").click(function(e) {
		e.preventDefault();

		var position = $($(this).attr("href")).offset().top;
		var navHeight = $('.navbar').innerHeight()
		
		$("body, html").animate({
			scrollTop: position - navHeight
		}, 1000);
	});
});