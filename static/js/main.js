(function(){


    $(window).on('load', function() {
        $('.item').first().addClass('active');
    });




    // $('.toggle-nav').click(function() {
    //     // Calling a function in case you want to expand upon this.
    //     toggleNav();
    // $('#site-menu').css('visibility', 'visible')
    //
    // });

    // $(document).keyup(function(e) {
    //     if (e.keyCode == 27) {
    //         if ($('#site-wrapper').hasClass('show-nav')) {
    //             // Assuming you used the function I made from the demo
    //             toggleNav();
    //         }
    //     } 
    // });


    centerElement('.album-cover-text');

    $(window).on('resize', function() {
        
        centerElement('.album-cover-text');
    });


/*=====================================================
    var fromTop = $('#photo-filters').offset().top;
    var filtersHeight = $('#photo-filters').height();

    $(window).on('scroll', function() {
        if ($(window).scrollTop() > fromTop) {
            $('#photo-filters').addClass('fixed');
            $('.photo-thumbnails').css('margin-top', filtersHeight);

        } else {
            $('#photo-filters').removeClass('fixed');
            $('.photo-thumbnails').css('margin-top', 0);
        }

    });

    $(window).on('resize',function(){
        fromTop = $('#photo-filters').offset().top;
        filtersHeight = $('#photo-filters').height();
        
    })
==========================================================*/




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


})();


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

