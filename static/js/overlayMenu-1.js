(function() {
	var triggerBttn = document.getElementById( 'trigger-overlay' ),
		overlay = document.querySelector( 'div.overlay' ),
		// closeBttn = overlay.querySelector( 'button.overlay-close' );
		transEndEventNames = {
			'WebkitTransition': 'webkitTransitionEnd',
			'MozTransition': 'transitionend',
			'OTransition': 'oTransitionEnd',
			'msTransition': 'MSTransitionEnd',
			'transition': 'transitionend'
		},
		transEndEventName = transEndEventNames[ Modernizr.prefixed( 'transition' ) ],
		support = { transitions : Modernizr.csstransitions };

	function toggleOverlay() {
		if( classie.has( overlay, 'open' ) ) {
			classie.remove( overlay, 'open' );
			classie.add( overlay, 'close' );
      // $('#logo').css('color', '#81d8d0');
      $('.button-toggle-navigation').removeClass('special');
      $('body').removeClass('body-fixed');

			// var onEndTransitionFn = function( ev ) {
			// 	if( support.transitions ) {
			// 		if( ev.propertyName !== 'visibility' ) return;
			// 		this.removeEventListener( transEndEventName, onEndTransitionFn );
			// 	}
			// 	classie.remove( overlay, 'close' );
			// };

			// if( support.transitions ) {
			// 	overlay.addEventListener( transEndEventName, onEndTransitionFn );
			// }
			// else {
			// 	onEndTransitionFn();
			// }
				classie.remove( overlay, 'close' );
		}
		else if( !classie.has( overlay, 'close' ) ) {
			classie.add( overlay, 'open' );
      // $('#logo').css('color', '#fff');
      $('.button-toggle-navigation').addClass('special');
      $('body').addClass('body-fixed');
		}
	}

	triggerBttn.addEventListener( 'click', toggleOverlay );
	// closeBttn.addEventListener( 'click', toggleOverlay );
})();
