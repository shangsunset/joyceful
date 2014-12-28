$(function(){

    var lastScrollTop = 0;
    $(window).on('scroll', function(){
      console.log('haha');
      var st = $(this).scrollTop();
      if (st > lastScrollTop){
        // downscroll code
        console.log("down");
      } else {
        // upscroll code
        console.log("up");
      }
      lastScrollTop = st;
    });



    $(window).on('load', function() {
        $('.item').first().addClass('active');
    });
        $('.carousel-indicators li').first().addClass('active');

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

