
/**
 * Actividades
 * @namespace managers.actividad.services
 */
(function () {
    'use strict';

    angular
        .module('managers.actividad.services')
        .factory('Actividades', Actividades);

    Actividades.$inject = ['$http'];

    function Actividades($http) {
        var Actividades = {
            all: all,
            create: create,
            get: get,
            modificar: modificar

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

    }
})();