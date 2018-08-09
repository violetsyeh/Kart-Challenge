"use strict";

function replaceStatus(results) {
    var status = results;
    $('#kart-status').html(status);
    console.log("Finished replaceStatus");
}

function updateStatus() {
    $.get('/add-to-kart', replaceStatus);
    console.log("Finished sending AJAX");
}

$('#tags').on('click', updateStatus);