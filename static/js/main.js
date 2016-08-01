// js file
function checkForChanges() {
    var $element = $("#nav");

    if ($element.css('height') != $('#messages').css('margin-top')) {
        $('#messages').css("margin-top", $element.height() + 10);
    }

    setTimeout(checkForChanges, 500);
}

$(document).ready(function() {
    checkForChanges();

});
