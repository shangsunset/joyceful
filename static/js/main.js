(function(){


    $(window).on('load', function() {
        $('.item').first().addClass('active');
    });


    //menu toggle
    $('.toggle-nav').click(function() {
        // Calling a function in case you want to expand upon this.
        toggleNav();
    $('#site-menu').css('visibility', 'visible')

    });

    $(document).keyup(function(e) {
        if (e.keyCode == 27) {
            if ($('#site-wrapper').hasClass('show-nav')) {
                // Assuming you used the function I made from the demo
                toggleNav();
            }
        } 
    });


    centerElement('.album-cover-text');

    $(window).on('resize', function() {
        
        centerElement('.album-cover-text');
    })


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

var GammaSettings = {
        // order is important!
        viewport : [ {
            width : 1200,
            columns : 5
        }, {
            width : 900,
            columns : 4
        }, {
            width : 500,
            columns : 3
        }, { 
            width : 320,
            columns : 2
        }, { 
            width : 0,
            columns : 2
        } ]
};

    Gamma.init( GammaSettings );



    $('.contact-form').on('submit', function() {

        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            dataType: 'json',
            url: $(this).attr('action'), // the file to call
            success: function(response) {
                $('.overlay').fadeIn(1000, function() {
                    // $(this).css('z-index', 0)
                })
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


function rgb2hex(rgb) {
    if (/^#[0-9A-F]{6}$/i.test(rgb)) return rgb;

    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    function hex(x) {
        return ("0" + parseInt(x).toString(16)).slice(-2);
    }
    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
}

function getContrastYIQ(hexcolor){
    var r = parseInt(hexcolor.substr(0,2),16);
    var g = parseInt(hexcolor.substr(2,2),16);
    var b = parseInt(hexcolor.substr(4,2),16);
    var yiq = ((r*299)+(g*587)+(b*114))/1000;
    return (yiq >= 128) ? 'black' : 'white';
}


//postions of album cover text
function centerElement(target) {

    var element = $(target);
    var elementHeight = element.height();
    var windowHeight = $(window).height();
    var elementPosTop = windowHeight/2-elementHeight/2 

    var elementWidth = element.width();
    var windowWidth = $(window).width();
    var elementPosLeft = windowWidth/2-elementWidth/2 

    element.css({left: elementPosLeft, top: elementPosTop})
}

