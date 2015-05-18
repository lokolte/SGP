
/**
 * Flujos
 * @namespace managers.actividad.services
 */
(function () {
    'use strict';

    angular
        .module('managers.actividad.services')
        .factory('Actividades', Actividades);

    Actividades.$inject = ['$http', '$cookies'];

    function Actividades($http, $cookies) {
        var Actividades = {
            all: all,
            create: create,
            get: get,
            modificar: modificar
            /*setAcCookie: setFlujoCookie,
            getFlujoCookie: getFlujoCookie,
            isExistFlujo: isExistFlujo,
            deleteFlujoCookie: deleteFlujoCookie*/
        };

        return Actividades;

        function all() {
            return $http.get('/api/flujos/');
        }

        function create(content) {
            return $http.post('/api/flujos/', {
                content: content //proyecto
            });
        }

        function get(id_flujo) {
            return $http.get('/api/flujos/' + id_flujo);
        }

        function modificar(id_flujo) {
            return $http.put('/api/flujos/' + id_flujo);
        }

        /*function setFlujoCookie(flujo){
            $cookies.byFlujo = JSON.stringify(flujo);
            console.log(getFlujoCookie());
        }

        function getFlujoCookie(){
            if(!isExistFlujo()) {
                return ;
            }
            console.log('hola json: '+angular.toJson($cookies.byFlujo));
            return JSON.parse($cookies.byFlujo);
        }

        function isExistFlujo(){
            return !!$cookies.byFlujo;
        }

        function deleteFlujoCookie(){
            delete $cookies.byFlujo;
        }*/

    }
})();