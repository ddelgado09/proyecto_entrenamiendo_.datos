$(function() {
    $('button.tablinks').click((e) => {
        var tabla = e.currentTarget.value;
        $.getJSON($SCRIPT_ROOT + '/ver_datos', {
            tabla: tabla
        }, (data) => {
            console.log(data);
        })
    })
});