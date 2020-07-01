var _system = (function() {
    var esconderOpinion = function(table) {
        num_rows = $('table#table-' + table).find('tr').length;
        $('table#table-' + table).find('td').get().forEach((e) => {
            var text = $(e).html();
            if(text.trim().length > 80)
            {
                var new_text = text.trim().slice(0, 80) + '... <a href="#" class="enlace-opinion" data-opinion="' + text + '">Ver más</a>';
                $(e).html(new_text);
            }
        })
    }

    var mostrarTabla = function(e) {
        openLoader();
        $('.tablinks').removeClass('active');
        $('table').removeClass('active');
        var tabla = e.currentTarget.value;
        esconderOpinion(tabla);
        $('table.table').hide();
        $('table#table-' + tabla).show();
        $(e.currentTarget).addClass('active');
        $('table#table-' + tabla).addClass('active');
        closeLoader();
    }

    var buscarDato = function(e) {
        var input, filter, table, tr, td, i, txtValue;
        input = $(e.currentTarget);
        filter = input.val().toUpperCase();
        table = $('table.active');
        tr = table.find('tr').get();

        for(i = 0; i < tr.length; ++i)
        {
            num_cols = $(tr[i]).find('td').length;
            for(j = 0; j < num_cols; ++j)
            {
                td = $(tr[i]).find('td').get()[j];
                if(td)
                {
                    txtValue = $(td).html();
                    if(txtValue.toUpperCase().indexOf(filter) > -1)
                    {
                        tr[i].style.display = "";
                    }
                    else
                    {
                        tr[i].style.display = "none";
                    }
                }
            }
        }
    }

    var cerrarModal = function(e)
    {
        var element = $(e.currentTarget);
        var modal = element.parents('.modal');
        modal.hide();
    }

    return {
        esconderOpinion: esconderOpinion,
        mostrarTabla: mostrarTabla,
        buscarDato: buscarDato,
        cerrarModal: cerrarModal
    }
})(jQuery);

$(document).ready(() => {
    $('.tablinks').click(_system.mostrarTabla);
    $('#search_value').keyup(_system.buscarDato);
    $('span.close').click(_system.cerrarModal);

    $('.table').on('click', '.enlace-opinion', (e) => {
        var data = $(e.currentTarget);
        var opinion = data.attr('data-opinion');
        $('#modal-opinion p.contenido').html(opinion);
        $('#modal-opinion').show();
    });
});