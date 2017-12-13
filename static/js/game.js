var selected, number;
$(document).ready(function() {
    selected = undefined;
    number = undefined;

    $(".table-inner tr td").each(function(index, element) {
        if ($(this).text()) {
            $(this).css('background-color', '#A9C1C3');
            $(this).addClass('immutable');
        }
    });

    $(".table-inner td").on('click', function() {
        if ($(this).text() == '' && number != 'delete') {
            toggle($(this));
        } else if ((!$(this).hasClass('immutable')) && number == 'delete') {
            number = '';
            toggle($(this));
        }
    });

    $(".btn-secondary").on('click', function() {
        number = $(this).text();
        // $(this).toggleClass("btn-secondary btn-primary");
    });
});


function toggle(element) {
   if (selected != undefined && selected != element) {
      untoggle(selected);
   }
   selected = element;

   if (number != undefined) {
       selected.text(number);
       number = undefined;
   } else {
       untoggle(selected);
   }

   element.css('background-color', '#3D9EFD');
}

function untoggle(element) {
    element.css('background-color', 'white');
}