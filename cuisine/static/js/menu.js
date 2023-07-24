// kaz_national_cuisine/cuisine/static/js/menu.js

$(document).ready(function() {
    // Smooth scroll to dish details when "View Details" button is clicked
    $('a.btn-orange').click(function(e) {
      // Check if the link is pointing to the current page (using regex)
      var currentUrlRegex = new RegExp(window.location.href + '$');
      if (!currentUrlRegex.test(this.href)) {
        // If the link points to a different page, let it navigate normally
        return;
      }
  
      // Prevent the default behavior (following the link)
      e.preventDefault();
  
      // Extract the slug from the URL using regex
      var slug = this.href.match(/\/dish\/(.+)\//)[1];
  
      // Check if the element with the corresponding slug as its ID exists
      if ($('#' + slug).length > 0) {
        // Element with the matching ID exists, scroll to it
        $('html, body').animate({
          scrollTop: $('#' + slug).offset().top
        }, 1000);
      }
    });
  
    // Fade in effect on dish cards when hovering
    $('.card').hover(function() {
      $(this).css('transform', 'scale(1.05)');
    }, function() {
      $(this).css('transform', 'scale(1)');
    });
  });
  