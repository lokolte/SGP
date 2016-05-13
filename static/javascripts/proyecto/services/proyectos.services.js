/**
 * Proyectos
 * @namespace managers.proyecto.services
 */
(function () {
    'use strict';

    angular
        .module('managers.proyecto.services')
        .factory('Proyectos', Proyectos);

    Proyectos.$inject = ['$http', '$cookies', 'Authentication'];

    function Proyectos($http, $cookies, Authentication) {
        var datos;

        var Proyectos = {
            all: all,
            create: create,
            get: get,
            modificar: modificar,
            suspender: suspender,

            setProyectoCookie: setProyectoCookie,
            getProyectoCookie: getProyectoCookie,
            isExistProyecto: isExistProyecto,
            deleteProyectoCookie: deleteProyectoCookie,
            setProyectosCookie: setProyectosCookie,
            isProyectosCookie: isProyectosCookie,
            getProyectosCookie: getProyectosCookie,
            deleteProyectosCookie: deleteProyectosCookie
        };

        return Proyectos;

        function all() {
            var userinfo = Authentication.getAuthenticatedUsuario();
            return $http.post('/api/user/' + userinfo.id + '/proyectos/');
        }

        function create(content) {
            console.log('creando... Nombre proyecto: ' + content.nombre);
            console.log(content);
            return $http.post('/api/proyectos/', content);
        }

        function get(id) {
            return $http.get('/api/proyectos/' + id + '/');
        }

        function modificar(id, content) {
            return $http.put('/api/proyectos/' + id + '/', content);
        }

        function suspender(id){
            return $http.delete('/api/proyectos/' + id + '/');
        }

        function setProyectoCookie(proyecto) {
            $cookies.putObject('byProject', proyecto);//.byProject = JSON.stringify(proyecto);
        }

        function isExistProyecto() {
            return !!$cookies.getObject('byProject');
        }

        function getProyectoCookie() {
            if (!isExistProyecto()) {
                return;
            }

            return $cookies.getObject('byProject');//JSON.parse($cookies.byProject);
        }

        function deleteProyectoCookie() {
            //delete $cookies.byProject;
            $cookies.remove('byProject');
        }

        function setProyectosCookie(proyectos) {
            $cookies.putObject('proyectos', proyectos);
        }

        function isProyectosCookie() {
            return !!$cookies.getObject('proyectos');
        }

        function getProyectosCookie() {
            if (!isProyectosCookie()) {
                return;
            }

            return $cookies.getObject('proyectos');
        }

        function deleteProyectosCookie() {
            $cookies.remove('proyectos');
        }
    }
})();