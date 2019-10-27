
new LazyLoad({
	elements_selector: ".lazy",
	threshold: 0
});

(function($){"use strict";
	var isHover = false;
	var navbarHeight = $("#main-navbar").outerHeight();
	var fixedNavbar = false;

	if ( $("#main-navbar").hasClass("fixed-top") || $("#main-navbar").hasClass("sticky-top") ) {
		fixedNavbar = true;
	}


	// collapse - page.jsFooterInline.5.2
	var collapse = $( ".collapsible-accordion" );
	if ( collapse.length && window.location.hash ) {
		collapse.removeClass("show");
		var hashArr = window.location.hash.split('c'),
			coll = $('#collapse-'+hashArr[1]);
		if (coll.length) {
			$('#collapse-'+hashArr[1]).addClass('show');
			var offsetSize = 0;
			if ( fixedNavbar ) {
				offsetSize = navbarHeight;
			}
			var collAnchor = '#collapse-'+hashArr[1];
			$("html, body").stop().animate({
				scrollTop: $(collAnchor).offset().top-offsetSize
			}, 1500, "easeInOutExpo");
		}
	}

	// collapsible active scroll to top
	$('.collapse').on('shown.bs.collapse', function(e) {
	  var $card = $(this).closest('.card');
	  if ( $card.length ) {
		$('html,body').animate({
			scrollTop: $card.offset().top-100
		}, 500);
	  }
	});

	// toast active
	var toast = $('.toast');
	if ( toast.length ) {
		$('.toast').toast('show');
	}


	// news - improved back links - page.jsFooterInline.5.3
	if ($(".news-backlink-wrap a").length > 0) {
		if(document.referrer.indexOf(window.location.hostname) != -1) {
			var buttontext = $(".news-backlink-wrap a").text();
			$(".news-backlink-wrap a").attr("href","javascript:history.back();").text(buttontext);
		}
	}


	// loading Spinner - page.jsFooterInline.5.4
	$(window).bind("load", function() {
	    $('#status').fadeOut();
	    $('#site-preloader').delay(350).fadeOut('slow');
	});


	// lightbox - page.jsFooterInline.5.5
	baguetteBox.run(".gallery, .image-gallery");


	// dropdown menu - page.jsFooterInline.5.6
	$(".dropdown-menu a.dropdown-toggle").on("click", function() {
		if (!$(this).next().hasClass("show")) {
			$(this).parents(".dropdown-menu").first().find(".show").removeClass("show");
		}
		var $subMenu = $(this).next(".dropdown-menu");
		$subMenu.toggleClass("show");

		$(this).parents("li.nav-item.dropdown.show").on("hidden.bs.dropdown", function() {
			$(".dropdown-submenu .show").removeClass("show");
		});

		return false;
	});


	// link to top - page.jsFooterInline.5.8
	var offset = 220;
	var duration = 500;
	$(window).scroll(function() {
		if ($(this).scrollTop() > offset) {
			$(".back-to-top").fadeIn(duration);
		} else {
			$(".back-to-top").fadeOut(duration);
		}
	});
	$(".back-to-top").click(function(event) {
		event.preventDefault(event);
		$("html, body").animate({scrollTop: 0}, duration);
		return false;
	});


	// sticky footer - page.jsFooterInline.5.9
	var footerHeight = $("#page-footer").outerHeight()-8,
		footerExtraHeight = 0;

	if ( footerExtraHeight > 0 ) {
		footerHeight += footerExtraHeight;
	}

	if ( $("#page-footer").hasClass("footer-sticky") ) {
		$("body").css("padding-bottom", footerHeight+"px");
	}


	// carousel - page.jsFooterInline.5.10
	var carousel = $( ".carousel .carousel-inner .carousel-item:first-child" );
	if ( carousel.length ) {
		carousel.addClass( "active" );
	}

	var cardSlider = $( ".carousel.card-slider" );
	if ( cardSlider.length ) {
		$(".carousel.card-slider").on("slide.bs.carousel", function(e) {
			var $e = $(e.relatedTarget);
			var idx = $e.index();
			var itemsPerSlide = 3;
			var totalItems = $(".carousel-item").length;

			if (idx >= totalItems - (itemsPerSlide - 1)) {
				var it = itemsPerSlide - (totalItems - idx);
				for (var i = 0; i < it; i++) {
					if (e.direction == "left") {
						$(".carousel-item")
						.eq(i)
						.appendTo(".carousel-inner");
					} else {
						$(".carousel-item")
						.eq(0)
						.appendTo(".carousel-inner");
					}
				}
			}
		});
	}


	// nav tab - page.jsFooterInline.5.12
	var tab = $( ".tab-content .tab-pane:first-child" );
	if ( tab.length ) {
		if ( window.location.hash ) {
			var tabHashArr = window.location.hash.split('c');
			$('.nav[role="tablist"] a[href="#tab-content-'+tabHashArr[1]+'"]').tab('show');
			var tabOffsetSize = 30;
			if ( fixedNavbar ) {
				tabOffsetSize = navbarHeight+30;
			}
			var tabAnchor = '#tab-'+tabHashArr[1];

			if ($(tabAnchor).length) {
				$("html, body").stop().animate({
					scrollTop: $(tabAnchor).offset().top-tabOffsetSize
				}, 1500, "easeInOutExpo");
			}

		} else {
			tab.addClass( "show active" );
		}
	}


	// Shrinking Navbar on scrolling - page.jsFooterInline.5.61
	var navShrinkColorschemes = $('#main-navbar').data('shrinkcolorschemes'),
		navShrinkColor = $('#main-navbar').data('shrinkcolor'),
		navColorschemes = $('#main-navbar').data('colorschemes'),
		navColor = $('#main-navbar').data('color');

	$(window).scroll(function() {
		if ($("#main-navbar").offset().top > 100) {
			$("#main-navbar").removeClass("py-5").removeClass(navColorschemes).removeClass(navColor)
			.addClass("navbar-shrink").addClass(navShrinkColor).addClass(navShrinkColorschemes);
		} else {
			$("#main-navbar").addClass("py-5").removeClass("navbar-shrink").removeClass(navShrinkColor).removeClass(navShrinkColorschemes)
			.addClass(navColorschemes).addClass(navColor);
		}
	});

})(jQuery);