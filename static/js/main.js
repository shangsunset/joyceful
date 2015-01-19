$(function(){


  // Hide Header on on scroll down
  var didScroll;
  var lastScrollTop = 0;
  var delta = 5;
  var navbarHeight = $('.top-menu-bar').outerHeight();

  $(window).scroll(function(event){
      didScroll = true;
  });



  setInterval(function() {
      if (didScroll) {
          hasScrolled();
          didScroll = false;
      }
  }, 250);

  function hasScrolled() {
      var st = $(this).scrollTop();
      
      // Make sure they scroll more than delta
      if(Math.abs(lastScrollTop - st) <= delta)
          return;
      
      // If they scrolled down and are past the navbar, add class .nav-up.
      // This is necessary so you never see what is "behind" the navbar.
      if (st > lastScrollTop && st > navbarHeight){
          // Scroll Down
          $('.top-menu-bar').removeClass('nav-down').addClass('nav-up');
      } else {
          // Scroll Up
          if(st + $(window).height() < $(document).height()) {
              // $('.top-menu-bar').css('background', '#fff');
              // $('.top-menu-bar').css('color', '#81d8d0');

              $('.top-menu-bar').removeClass('nav-up').addClass('nav-down');
          }
      }
      
      lastScrollTop = st;
  }



  // if ($(window).scrollTop() === 0) {
  //   $('.top-menu-bar').css('background', 'transparent');
  // }





  $('.button-toggle-navigation').on('click', function() {
    $(this).toggleClass('isActive');

  });




    $(window).on('load', function() {
        $('.item').first().addClass('active');
        $('.carousel-indicators li').first().addClass('active');
        $('ol.slides li').first().addClass('current');
    });

    $('.carousel').carousel({
      pause: "false"
    });




    $('.contact-form').on('submit', function() {

        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            dataType: 'json',
            url: $(this).attr('action'), // the file to call
            success: function(response) {
                $('.overlay').fadeIn(1000, function() {
                    // $(this).css('z-index', 0)
                });
                $('.alert-success').css({'display': 'block'});
                $('.alert-info').css({'display': 'none'});
                $('.form-control').val('');


            },
            error: function(response) {
                $('.alert-danger').css({'display': 'block'});
                $('.alert-info').css({'display': 'none'});
            }
        });
        return false;
    });


    var $container = $('#album-covers-index');
    // initialize Masonry after all images have loaded
    $container.imagesLoaded(function() {
      $container.masonry({
        itemSelector: '.single-album-cover',
        // columWidth: '5%',
        isFitWidth: true
      });
    });


    var $containerPswp = $('.pswp-gallery');
    $containerPswp.imagesLoaded( function() {
      $containerPswp.masonry({
        itemSelector: '.pswp-gallery figure',
        // columWidth: 500,
        isFitWidth: true
      
      });
    });


});


function toggleNav() {
    if ($('#site-wrapper').hasClass('show-nav')) {
        // Do things on Nav Close
        $('#site-wrapper').removeClass('show-nav');
    } else {
        // Do things on Nav Open
        $('#site-wrapper').addClass('show-nav');
    }
	$('.menu-icon').toggleClass('fa-angle-double-left, fa-angle-double-right');

}




//postions of album cover text
function centerElement(target) {

    var element = $(target);
    var elementHeight = element.height();
    var windowHeight = $(window).height();
    var elementPosTop = windowHeight/2-elementHeight/2;

    var elementWidth = element.width();
    var windowWidth = $(window).width();
    var elementPosLeft = windowWidth/2-elementWidth/2;

    // element.css({left: elementPosLeft, top: elementPosTop})
    element.css({left: elementPosLeft});
}

