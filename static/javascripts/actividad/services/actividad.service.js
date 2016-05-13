
/**
 * Actividades
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
            modificar: modificar,

            setActividadCookie: setActividadCookie,
            getActividadCookie: getActividadCookie,
            isExistActividad: isExistActividad,
            deleteActividadCookie: deleteActividadCookie,

            setActividadesCookie: setActividadesCookie,
            getActividadesCookie: getActividadesCookie,
            isActividadesCookie: isActividadesCookie,
            deleteActividadesCookie: deleteActividadesCookie
        };

        return Actividades;

        function all() {
            return $http.get('/api/actividades/');
        }

        function create(content) {
            return $http.post('/api/actividades/', {
                content: content
            });
        }

        function get(id_actividad) {
            return $http.get('/api/actividades/' + id_actividad);
        }

        function modificar(id_actividad) {
            return $http.put('/api/actividades/' + id_actividad);
        }

        function setActividadCookie(act){
            $cookies.putObject('Actividad', act);
        }

        function isExistActividad(){
            return !!$cookies.getObject('Actividad');
        }

        function getActividadCookie(){
            if(!isExistActividad()) {
                return ;
            }

            return $cookies.getObject('Actividad');
        }

        function deleteActividadCookie(){
            $cookies.remove('Actividad');
        }

        function setActividadesCookie(actividades){
             $cookies.putObject('Actividades', actividades);
        }

        function isActividadesCookie(){
             return !!$cookies.getObject('Actividades');
        }

        function getActividadesCookie(){
             if(!isActividadesCookie()){
                return ;
             }

            return $cookies.getObject('Actividades');
        }

        function deleteActividadesCookie(){
            $cookies.remove('Actividades');
        }

    }
})();