function success(response, status) {
    $('#answer').text(response.answer);
}

function error(response, status) {
    $('#answer').text(response.responseJSON.error);
}

function getData() {
    return {
        'A': parseFloat($('#input-A').val()),
        'B': parseFloat($('#input-B').val())
    };
}

function getUrl(event) {
    let action = $(event.target).data('action');
    return 'http://localhost:8000/' + action + '/';
}

function calculate(event) {
    $.ajax({
        url: getUrl(event),
        method: 'post',
        data: JSON.stringify(getData()),
        contentType: 'application/json',
        dataType: 'json',
        success: success,
        error: error
    });
}

function setUpButtons() {
    ['add', 'multiply', 'divide', 'subtract'].forEach(function(action) {
        let id = '#' + action;
        $(id).click(calculate);
    });
}

function initContent() {
    $("#container").html(`<h1 class="text-center my-3">Calculator</h1>
<div id="answer" class="text-center bg-light"></div>
<div id="inputs" class="form-inline justify-content-center mt-3">
    <input type="text" id="input-A" class="form-control" placeholder="Введите число A">
    <input type="text" id="input-B" class="form-control ml-2" placeholder="Введите число B">
</div>
<div id="controls" class="text-center mt-3">
    <button type="button" id="add" class="btn btn-primary" data-action="add">Add</button>
    <button type="button" id="subtract" class="btn btn-primary" data-action="subtract">Subtract</button>
    <button type="button" id="multiply" class="btn btn-primary" data-action="multiply">Multiply</button>
    <button type="button" id="divide" class="btn btn-primary" data-action="divide">Divide</button>
</div>`);
}

$(document).ready(function() {
    initContent();
    setUpButtons();
});
