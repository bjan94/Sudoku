var selected, number, numButton, board;
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


    board = []
    for (var i = 0; i < 9; i++) {
        board[i] = [];
        for (var j = 0; j < 9; j++) {
            var indexId = '#' + i + '' + j;
            if ($(indexId).text()) {
                board[i][j] = parseInt($(indexId).text());
            } else {
                board[i][j] = 0;
            }
        }
    }
});

function toggleBox(element) {
    if (selected != undefined && selected != element) {
        untoggleBox(selected);
    }
    selected = element;
    element.css('background-color', '#3D9EFD');

    if (number != undefined) {
        fillNumber(selected, number);
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
        fillNumber(selected, number);
    }
}

function fillNumber(selected, num) {
    if (num != 0) {
        selected.text(num);
    } else { // delete button
        selected.text('');
    }

    changeBoard();

    if (numButton) {
        numButton.toggleClass("btn-primary btn-secondary");
    }

    number = undefined;
    numButton = undefined;
}

function changeBoard() {
    var index = selected.attr('id');
    var i = index.split('')[0];
    var j = index.split('')[1];

    validate(i, j, number, function() {
        untoggleBox(selected);
    });
}

function untoggleBox(element) {
    if ($("#game-message").hasClass('alert-danger')) {
        element.css('background-color', '#F8D7DB');
    } else {
        console.log('here');
        element.css('background-color', 'white');
    }

    selected = undefined;
}

function validate(i, j, val, callback) {
    sendData = {i: i, j: j, val: val};
    $.post('/validate', sendData, function(response) {
        if (response.success) {
            $('#game-message').text('');
            $('#game-message').removeClass('alert-danger');
        } else if (val != 0) {
            $('#game-message').addClass('alert-danger');
            $('#game-message').text('Incorrect placement. Try Again');
        }
    }).done(callback);
}