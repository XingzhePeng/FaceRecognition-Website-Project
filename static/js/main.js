//delayed, ande then jump to a new page
function jump(url) {
	var delay = setTimeout(function () {
		window.location.href = url;
    },350);
}
function upload() {
	$("#file_form").submit();
}
function upload_2(){
	$(".file").trigger("click");
}
(function($) {
	"use strict";
	var cfg = {
		defAnimation   : "fadeInUp",    // default css animation
		scrollDuration : 800,           // smoothscroll duration
	},

	$WIN = $(window);

   // Add the User Agent to the <html>
   // will be used for IE10 detection (Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0))
	var doc = document.documentElement;
	doc.setAttribute('data-useragent', navigator.userAgent);

	/* Menu on Scrolldown
	 * ------------------------------------------------------ */
	var ssMenuOnScrolldown = function() {

		var menuTrigger = $('#header-menu-trigger');

		$WIN.on('scroll', function() {

			if ($WIN.scrollTop() > 150) {				
				menuTrigger.addClass('opaque');
			}
			else {				
				menuTrigger.removeClass('opaque');
			}

		}); 
	};
	
  	/* OffCanvas Menu
	 * ------------------------------------------------------ */
   var ssOffCanvas = function() {

	       var menuTrigger = $('#header-menu-trigger'),
	       nav             = $('#menu-nav-wrap'),
	       closeButton     = nav.find('.close-button'),
	       siteBody        = $('body'),
	       mainContents    = $('section, footer');

		// open-close menu by clicking on the menu icon
		menuTrigger.on('click', function(e){
			e.preventDefault();
			menuTrigger.toggleClass('is-clicked');
			siteBody.toggleClass('menu-is-open');
		});

		// close menu by clicking the close button
		closeButton.on('click', function(e){
			e.preventDefault();
			menuTrigger.trigger('click');	
		});

		// close menu clicking outside the menu itself
		siteBody.on('click', function(e){		
			if( !$(e.target).is('#menu-nav-wrap, #header-menu-trigger, #header-menu-trigger span') ) {
				menuTrigger.removeClass('is-clicked');
				siteBody.removeClass('menu-is-open');
			}
		});

   };
  /* Smooth Scrolling
	* ------------------------------------------------------*/
	var ssSmoothScroll_1 = function() {

		$('.smoothscroll_1').on('click', function (e) {
			var target = this.hash,
			$target    = $(target);

		 	e.preventDefault();
		 	e.stopPropagation();	   	

	    	$('html, body').stop().animate({
	       	'scrollTop': $target.offset().top
	      }, cfg.scrollDuration, 'swing').promise().done(function () {

	      	// check if menu is open
	      	if ($('body').hasClass('menu-is-open')) {
					$('#header-menu-trigger').trigger('click');
				}

	      	window.location.hash = target;
	      });
	  	});

	};


	var ssSmoothScroll = function() {

		$('.smoothscroll').on('click', function (e) {
			var _this = $(this);

		 	e.preventDefault();
		 	e.stopPropagation();
		 	if ($('body').hasClass('menu-is-open')) {
					$('#header-menu-trigger').trigger('click');
				};
		 	jump(_this.attr("href"));

	  	});

	};


  /* Back to Top
	* ------------------------------------------------------ */
	var ssBackToTop = function() {

		var pxShow  = 500,         // height on which the button will show
		fadeInTime  = 400,         // how slow/fast you want the button to show
		fadeOutTime = 400,         // how slow/fast you want the button to hide
		scrollSpeed = 300,         // how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'
		goTopButton = $("#go-top")

		// Show or hide the sticky footer button
		$(window).on('scroll', function() {
			if ($(window).scrollTop() >= pxShow) {
				goTopButton.fadeIn(fadeInTime);
			} else {
				goTopButton.fadeOut(fadeOutTime);
			}
		});
	};

  /* Initialize
	* ------------------------------------------------------ */
	(function ssInit() {

		ssMenuOnScrolldown();
		ssOffCanvas();
		ssSmoothScroll();
		ssBackToTop();
		ssSmoothScroll_1();

	})();
})(jQuery);

