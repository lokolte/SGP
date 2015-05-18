(function () {
    'use strict';

    angular
        .module('managers.sprint.services')
        .factory('Sprints', Sprints);

    Sprints.$inject = ['$http', '$cookies'];

    function Sprints($http, $cookies) {
        var Sprints = {
            all: all,
            create: create,
            get: get,
            modificar: modificar,
            setSprintCookie: setSprintCookie,
            isExistSprint: isExistSprint,
            getSprintCookie: getSprintCookie,
            deleteSprintCookie: deleteSprintCookie,
            agregarUserStory: agregarUserStory
        };

        return Sprints;

        function all() {
            return $http.get('/api/sprints/');
        }

        function create(content) {
            return $http.post('/api/sprints/', {
                content: content //proyecto
            });
        }

        function get(id) {
            return $http.get('/api/sprints/' + id);
        }

        function modificar(id) {
            return $http.put('/api/sprints/' + id);
        }

        function setSprintCookie(sprint){
            $cookies.bySprint = JSON.stringify(sprint);
        }

        function isExistSprint(){
            return !!$cookies.bySprint;
        }

        function getSprintCookie(){
            if(!isExistSprint()) {
                return ;
            }

            return JSON.parse($cookies.bySprint);
        }

        function deleteSprintCookie(){
            delete $cookies.bySprint;
        }

        function agregarUserStory(us){
            var s = getSprintCookie();
            s.duracionHoras = s.duracionHoras - us.tamanho;
            setSprintCookie(s);
        }

    }
})();