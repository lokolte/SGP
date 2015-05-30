/**
 * Utils
 * @namespace managers.utils.services
 */
(function () {
    'use strict';

    angular
        .module('managers.utils.services')
        .factory('Utils', Utils);

    Utils.$inject = [];

    function Utils() {
        var Utils = {
            toData: toData,
            toDataObject: toDataObject
        };

        return Utils;

        function toData(dia, mes, anho, hora, minuto, segundo) {
            var fecha = anho + '-' + mes + '-' + dia + ' ' + hora + ':' + minuto + ':' + segundo;
            console.log(fecha);
            return fecha;
        }

        function toDataObject(date){
            date = new Date();
            var fecha = date.getFullYear() + '-' + date.getTwoDigitMonth() + '-' + date.getTwoDigitDate() + ' ' + date.getTwoDigitHour() + ':' + date.getTwoDigitMinute() + ':' + date.getTwoDigitSecond();
            console.log(fecha);
            return fecha;
        }
    }
})();
