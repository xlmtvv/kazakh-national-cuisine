// kaz_national_cuisine/cuisine/static/js/menu.js

$(document).ready(function() {
    // Smooth scroll to dish details when "View Details" button is clicked
    $('a.btn-orange').click(function(e) {
      e.preventDefault();
      var target = $(this).attr('href'); // Get the full URL, e.g., '/dish/besh/'
  
      // Extract the slug from the URL (you may need to adjust this depending on your URL structure)
      var slug = target.split('/').filter(Boolean).pop();
  
      // Check if the element with the corresponding slug as its ID exists
      if ($('#' + slug).length > 0) {
        // Element with the matching ID exists, scroll to it
        $('html, body').animate({
          scrollTop: $('#' + slug).offset().top
        }, 1000);
      } else {
        // Element does not exist, handle the error (e.g., show an error message)
        console.error('Element with ID ' + slug + ' does not exist.');
      }
    });
  
    // Fade in effect on dish cards when hovering
    $('.card').hover(function() {
      $(this).css('transform', 'scale(1.05)');
    }, function() {
      $(this).css('transform', 'scale(1)');
    });
  });
  