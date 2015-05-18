/**
 * Created by lokolte on 16/05/15.
 */
/**
 * Flujos
 * @namespace managers.flujo.services
 */
(function () {
    'use strict';

    angular
        .module('managers.flujo.services')
        .factory('Flujos', Flujos);

    Flujos.$inject = ['$http', '$cookies'];

    function Flujos($http, $cookies) {
        var Flujos = {
            all: all,
            create: create,
            get: get,
            modificar: modificar,
            setFlujoCookie: setFlujoCookie,
            getFlujoCookie: getFlujoCookie,
            isExistFlujo: isExistFlujo,
            deleteFlujoCookie: deleteFlujoCookie
        };

        return Flujos;

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

        function setFlujoCookie(flujo){
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
        }

    }
})();