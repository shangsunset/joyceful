(function(){
    $.adaptiveBackground.run()

    $('.toggle-nav').click(function() {
        // Calling a function in case you want to expand upon this.
        toggleNav();

    });

    $(document).keyup(function(e) {
        if (e.keyCode == 27) {
            if ($('#site-wrapper').hasClass('show-nav')) {
                // Assuming you used the function I made from the demo
                toggleNav();
            }
        } 
    });


    menuColor();

    $('.carousel').carousel({
        pause: "false"
    });

    var scene = document.getElementById('scene');
    var parallax = new Parallax(scene);

    var color = document.getElementById("album_cover").style.backgroundColor;
    // var color = $('#album_cover').css("background-color");
    var albumCoverHex = rgb2hex(color);

})();

/*========================================
=            CUSTOM FUNCTIONS            =
========================================*/
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

function menuColor() {

        if ($('#album_cover>div').hasClass('ab-light')) {
            $('.top-menu-bar a').css('color', 'black');
            console.log('sdafasdfsdf');
        }
        else {
            $('.top-menu-bar a').css('color', 'white');
            console.log('darkkkkkk');

        }

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
