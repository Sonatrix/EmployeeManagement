jQuery(function ($) {
    'use strict';

    $('#bb-alert').on('click', function () {
        bootbox.alert({
            message: 'Hello world!',
            callback: function () {
            },
            className: 'bootbox-sm'
        });
    });
    $('#bb-confirm').on('click', function () {
        bootbox.confirm({
            message: 'Are you sure?',
            callback: function (result) {
            },
            className: 'bootbox-sm'
        });
    });
    $('#bb-prompt').on('click', function () {
        bootbox.prompt({
            title: 'What is your name?',
            callback: function (result) {
            }
        });
    });
    $('#bb-custom').on('click', function () {
        bootbox.dialog({
            message: 'I am a custom dialog',
            title: 'Custom title',
            buttons: {
                success: {
                    label: 'Success!',
                    className: 'btn-success',
                    callback: function () {
                    }
                },
                danger: {
                    label: 'Danger!',
                    className: 'btn-danger',
                    callback: function () {
                    }
                },
                main: {
                    label: 'Click ME!',
                    className: 'btn-primary',
                    callback: function () {
                    }
                }
            },
            className: 'bootbox-lg'
        });
    });
});
