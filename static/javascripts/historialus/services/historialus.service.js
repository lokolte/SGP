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
            $cookies.his = JSON.stringify(historialus);
            //$cookies.putObject('hist',historialus);
        }

        function isExistHistorial(){
            return !!$cookies.his;
            //!!$cookies.getObject('hist');
        }

        function getHistorialCookie(){
            if(!isExistHistorial()) {
                return ;
            }

            return JSON.parse($cookies.his);
            //return $cookies.getObject('historialuss');
        }

        function deleteHistorialCookie(){
            delete $cookies.his;
            //$cookies.remove('historialuss');
        }

    }
})();