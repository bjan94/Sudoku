var selected;
$(document).ready(function() {
   selected = undefined;
   $(".table-inner td").on('click', function() {
      toggle($(this));
   });
});

function toggle(element) {
   if (selected != undefined && selected != element) {
      untoggle(selected);
   }
   selected = element;
   element.css('background-color', '#3D9EFD');
}

function untoggle(element) {
   element.css('background-color', 'white');
}