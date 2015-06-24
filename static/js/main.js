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





    // $(window).on('load', function() {
    //     $('.item').first().addClass('active');
    //     $('.carousel-indicators li').first().addClass('active');
    //     $('ol.slides li').first().addClass('current');
    // });
    //
    // $('.carousel').carousel({
    //   pause: "false"
    // });
    //



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


    // var $container = $('.gridLoading');
    // // initialize Masonry after all images have loaded
    // $container.imagesLoaded(function() {
    //   $container.masonry({
    //     itemSelector: '.gridLoading figure',
    //     isFitWidth: true
    //   });
    // });


    var $containerPswp = $('.pswp-gallery');
    $containerPswp.imagesLoaded( function() {
      $containerPswp.masonry({
        itemSelector: '.pswp-gallery figure',
        columWidth: 250,
        isFitWidth: true

      });
    });


});





