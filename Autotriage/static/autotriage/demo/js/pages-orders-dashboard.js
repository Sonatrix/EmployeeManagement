jQuery(function ($) {
    var ordersChart;
    var salesChart;
    var avgOrderValueChart;

    function flotTooltip() {
        return $('<div></div>').css({
            position: 'absolute',
            display: 'none',
            border: '1px solid rgba(0, 0, 0, 0.4)',
            borderRadius: '3px',
            padding: '0.25em',
            'background-color': 'rgba(0, 0, 0, 0.8)',
            color: '#fff',
            fontSize: '12px'
        }).appendTo('body');
    }

    $('#tab-orders-tab').on('shown.bs.tab', function (e) {
        if (!ordersChart) {
            ordersChart = flotChart('#chart-orders', [
                ['02/2014', 20],
                ['03/2014', 10],
                ['04/2014', 35],
                ['05/2014', 70],
                ['06/2014', 20],
                ['07/2014', 20],
                ['08/2014', 89]
            ], 'Orders', '#1C2A3C', '', 0);
        }
    });

    $('#tab-avg-order-value-tab').on('shown.bs.tab', function (e) {
        if (!avgOrderValueChart) {
            avgOrderValueChart = flotChart('#chart-avg-order-value', [
                ['02/2014', 90.43 ],
                ['03/2014', 300.20],
                ['04/2014', 780.04],
                ['05/2014', 565.90],
                ['06/2014', 550.78],
                ['07/2014', 600.00],
                ['08/2014', 251.26]
            ], 'Avg. Order Value', '#26C281', '$', 2);
        }
    });

    if (!salesChart) {
        salesChart = flotChart('#chart-sales', [
            ['02/2014', 349],
            ['03/2014', 1100],
            ['04/2014', 692],
            ['05/2014', 175],
            ['06/2014', 450],
            ['07/2014', 1850],
            ['08/2014', 953]
        ], 'Sales', '#34A8DB', '$', 2);
    }


    function flotChart(selector, data, label, color, preUnit, round) {
        var plot = $.plot(selector, [
            {
                data: data,
                label: label,
                color: color,
                lines: {
                    show: true,
                    fill: true,
                    lineWidth: 2
                }
            }
        ],
            {
                series: {
                    points: {
                        show: true,
                        lineWidth: 2,
                        fill: true,
                        fillColor: '#ffffff',
                        symbol: 'circle',
                        radius: 5
                    },
                    shadowSize: 0
                },
                legend: {
                    position: 'nw'
                },
                grid: {
                    hoverable: true,
                    clickable: true,
                    borderColor: '#ddd',
                    borderWidth: 1,
                    labelMargin: 10,
                    backgroundColor: '#fff'
                },
                yaxis: {
                    color: '#edeff0'
                },
                xaxis: {
                    tickLength: 0,
                    mode: 'categories'
                }
            }
        );

        var prev = null;
        var $tooltip = flotTooltip();
        $(selector).bind('plothover', function (event, pos, item) {
            if (item) {
                var x = item.datapoint[0].toFixed(round),
                    y = item.datapoint[1].toFixed(round);
                if (prev != x + '_' + y) {
                    prev = x + '_' + y;

                    $tooltip.html(item.series.label + ': ' + preUnit + y);
                    $tooltip.css({top: item.pageY - $tooltip.height() - 20, left: item.pageX - $tooltip.width()})
                        .fadeIn(200);
                }
            } else {
                $tooltip.fadeOut(100);
                prev = null;
            }
        });

        $(selector).bind('plotclick', function (event, pos, item) {
            if (item) {
                plot.highlight(item.series, item.datapoint);
            }
        });
        return plot;
    }
});
