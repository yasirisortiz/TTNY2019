/*
 * This file is part of the "gridgallery" Extension for TYPO3 CMS.
 *
 * For the full copyright and license information, please read the
 * LICENSE file that was distributed with this source code.
 */

let gridgallery = {

	/**
	 * Initialize the grid gallery
	 */
	init: function () {
		gridgallery.loadGallery();
		gridgallery.lazyLoadImages();
		$(window).on('resize scroll', function () {
			gridgallery.lazyLoadImages();
		});
	},

	/**
	 * Load the gallery with justifiedGallery()
	 */
	loadGallery: function () {
		var ggInterval;
		ggInterval = setInterval(function () {
			$('.ce-gridgallery').each(function () {
				init($(this));
			});
		}, 100);

		function init(el) {
			if (el.is(':visible')) {
				el.justifiedGallery({
					rowHeight: $(this).data('row-height'),
					margins: $(this).data('margins')
				});
				clearInterval(ggInterval);
			}
		}
	},

	/**
	 * Load "unloaded" images if they are in the viewport
	 */
	lazyLoadImages: function () {
		$('.ce-gridgallery img.unloaded').each(function () {
			if (gridgallery.isInViewport($(this)) === true) {
				let src = $(this).attr('data-src');
				let srcset = $(this).attr('data-srcset');
				if (src !== undefined && src !== '') {
					$(this).attr('src', src).removeAttr('data-src');
				}
				if (srcset !== undefined && srcset !== '') {
					$(this).attr('srcset', srcset).removeAttr('data-srcset');
				}
				$(this).removeClass('unloaded');
			}
		});
	},

	/**
	 * Checks if an element is in the viewport
	 *
	 * @param      img        Image Object
	 * @returns    boolean    returns true if the image is in viewport
	 */
	isInViewport: function (img) {
		let elementTop = img.offset().top;
		let elementBottom = elementTop + img.outerHeight();
		let viewportTop = $(window).scrollTop();
		let viewportBottom = viewportTop + $(window).height();
		return elementBottom >= viewportTop && elementTop <= viewportBottom;
	}
};

$(document).ready(function () {
	gridgallery.init();
});
