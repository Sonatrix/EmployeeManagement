jQuery(function ($) {
    'use strict';
    $('[data-rel=datepicker]').datepicker({
        autoclose: true,
        todayHighlight: true
    });

    var $table = $('#table-orders');
    var table = $table.dataTable({
        bSortCellsTop: true,
        order: [
            [ 0, 'desc' ]
        ],
        columnDefs: [
            {
                'orderable': false,
                'targets': [5]
            },
            {
                width: '184px',
                targets: 3
            },
            {
                width: '200px',
                targets: 4
            }
        ]
    });
    var tableApi = table.api();

    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var colIdx = 3;
            var min = parseFloat($table.find('.filters td').eq(colIdx).find('[name$=from]').val());
            var max = parseFloat($table.find('.filters td').eq(colIdx).find('[name$=to]').val());
            var val = Number(data[colIdx].replace(/[^0-9\.]+/g, '')) || 0;

            if (( isNaN(min) && isNaN(max) ) ||
                ( isNaN(min) && val <= max ) ||
                ( min <= val && isNaN(max) ) ||
                ( min <= val && val <= max )) {
                return true;
            }
            return false;
        },
        function (settings, data, dataIndex) {
            var colIdx = 1;
            var $from = $table.find('.filters td').eq(colIdx).find('[name$=from]');
            var $to = $table.find('.filters td').eq(colIdx).find('[name$=to]');

            var min = NaN;
            var max = NaN;
            var val = NaN;
            if ($from.val().match(/\d{2}\/\d{2}\/\d{4}/)) {
                min = $from.data('datepicker').getDate();
            }
            if ($to.val().match(/\d{2}\/\d{2}\/\d{4}/)) {
                max = $to.data('datepicker').getDate();
            }
            if (data[colIdx].match(/\d{2}\/\d{2}\/\d{4}/)) {
                val = $.fn.datepicker.DPGlobal.parseDate(data[colIdx], $from.data('datepicker').format);
            }

            if (( isNaN(min) && isNaN(max) ) ||
                ( isNaN(min) && val <= max ) ||
                ( min <= val && isNaN(max) ) ||
                ( min <= val && val <= max )) {
                return true;
            }
            return false;
        }
    );
    // Reset search
    $table.find('.filters .filter-cancel').on('click', function (e) {
        e.preventDefault();
        $table.find('.filters td').find('input[type=text]').val('').trigger('change');
        $table.find('.filters td').find('select').select2('val', '').trigger('change');
        tableApi.draw();
        return false;
    });
    // Apply the search
    var $cells = $table.find('.filters td');
    filterColumnSimple(0, 'input');
    filterColumnSimple(2, 'input');
    filterColumnSimple(4, 'select');
    $cells.eq(1).find('input').on('keyup change', function () {
        tableApi.draw();
    });
    $cells.eq(3).find('input').on('keyup change', function () {
        tableApi.draw();
    });

    $('#table-orders_wrapper select.form-control').select2({minimumResultsForSearch: -1});

    function filterColumnSimple(colIdx, sel) {
        var $el = $cells.eq(colIdx).find(sel);
        $el.on('keyup change', function () {
            if (this.value) {
                if(this.tagName.toLowerCase() == 'select'){
                    tableApi.column(colIdx).search($(this).find('option:selected').text()).draw();
                }
                else {
                    tableApi.column(colIdx).search(this.value).draw();
                }
            }
            else {
                tableApi.column(colIdx).search('').draw();
            }
        });
        if ($el.val()) {
            if($el.prop('tagName').toLowerCase() == 'select'){
                tableApi.column(colIdx).search($el.find('option:selected').text()).draw();
            }
            else {
                tableApi.column(colIdx).search($el.val()).draw();
            }
        }
    }
});
