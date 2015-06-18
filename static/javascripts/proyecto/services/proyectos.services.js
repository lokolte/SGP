/**
 * Proyectos
 * @namespace managers.proyecto.services
 */
(function () {
    'use strict';

    angular
        .module('managers.proyecto.services')
        .factory('Proyectos', Proyectos);

    Proyectos.$inject = ['$http', '$cookies'];

    function Proyectos($http, $cookies) {
        var Proyectos = {
            all: all,
            create: create,
            get: get,
            modificar: modificar,
            setProyectoCookie: setProyectoCookie,
            getProyectoCookie: getProyectoCookie,
            isExistProyecto: isExistProyecto,
            deleteProyectoCookie: deleteProyectoCookie
        };

        return Proyectos;

        function all() {
            return $http.get('/api/proyectos/');
        }

        function create(content) {
            return $http.post('/api/proyectos/', {
                content: content //proyecto
            });
        }

        function get(id) {
            return $http.post('/api/proyectos/', {'id': id});
        }

        function modificar(id_proyecto) {
            return $http.put('/api/proyectos/' + id_proyecto);
        }

        function setProyectoCookie(proyecto){
            $cookies.byProject = JSON.stringify(proyecto);
        }

        function isExistProyecto(){
            return !!$cookies.byProject;
        }

        function getProyectoCookie(){
            if(!isExistProyecto()) {
                return ;
            }

            return JSON.parse($cookies.byProject);
        }

        function deleteProyectoCookie(){
            delete $cookies.byProject;
        }

    }
})();