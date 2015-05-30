/**
 * HistorialUS
 * @namespace managers.historialus.services
 */
(function () {
    'use strict';

    angular
        .module('managers.historialus.services')
        .factory('HistorialUS', HistorialUS);

    HistorialUS.$inject = ['$http', '$cookies'];

    function HistorialUS($http, $cookies) {

        var HistorialUS = {
            setHistorialCookie: setHistorialCookie,
            getHistorialCookie: getHistorialCookie,
            isExistHistorial: isExistHistorial,
            deleteHistorialCookie: deleteHistorialCookie
        };

        return HistorialUS;

        function setHistorialCookie(historialus){
            $cookies.byHistorial = JSON.stringify(historialus);
        }

        function isExistHistorial(){
            return !!$cookies.byHistorial;
        }

        function getHistorialCookie(){
            if(!isExistHistorial()) {
                return ;
            }

            return JSON.parse($cookies.byHistorial);
        }

        function deleteHistorialCookie(){
            delete $cookies.byHistorial;
        }

    }
})();