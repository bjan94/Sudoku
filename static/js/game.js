var selected, number, numButton;
$(document).ready(function() {
    selected = undefined;
    number = undefined;

    $(".table-inner tr td").each(function(index, element) {
        if ($(this).text()) {
            $(this).css('background-color', '#A9C1C3');
            $(this).addClass('fixed');
        }
    });

    $(".table-inner td").on('click', function() {
         if (!$(this).hasClass('fixed')) {
             toggleBox($(this));
         }
    });

    $(".btn-secondary").on('click', function() {
        toggleButton($(this));
    });



});

function toggleBox(element) {
    if (selected != undefined && selected != element) {
        untoggleBox(selected);
    }
    selected = element;
    element.css('background-color', '#3D9EFD');

    if (number != undefined) {
        fillNumber(selected, number, validate);
    }
}

function toggleButton(element) {
    number = element.text();

    if (element.attr('id') == 'delete') {
        number = 0;
    }

    if (numButton) {
        numButton.toggleClass("btn-primary btn-secondary");
    }

    element.toggleClass("btn-secondary btn-primary");
    numButton = element;

    if (selected) {
        fillNumber(selected, number, validate);
    }
}

function untoggleBox(element) {
   element.css('background-color', 'white');
   selected = undefined;
}

function fillNumber(selected, num, callback) {
    if (num != 0) {
        selected.text(num);
    } else {
        selected.text('');
    }

    untoggleBox(selected);

    if (numButton) {
        numButton.toggleClass("btn-primary btn-secondary");
    }

    number = undefined;
    numButton = undefined;

    callback();
}

function validate() {
    // console.log(table)
}