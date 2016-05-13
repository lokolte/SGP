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
            agregarUserStory: agregarUserStory,

            setSprintsCookie: setSprintsCookie,
            isExistSprints: isExistSprints,
            getSprintsCookie: getSprintsCookie,
            deleteSprintsCookie: deleteSprintsCookie
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
            $cookies.putObject('sprint', sprint);
        }

        function isExistSprint(){
            return !!$cookies.getObject('sprint');
        }

        function getSprintCookie(){
            if(!isExistSprint()) {
                return ;
            }

            return $cookies.getObject('sprint');//JSON.parse($cookies.bySprint);
        }

        function deleteSprintCookie(){
            //delete $cookies.bySprint;
            $cookies.remove('sprint');
        }

        function agregarUserStory(us){
            var s = getSprintCookie();
            s.duracionHoras = s.duracionHoras - us.tamanho;
            setSprintCookie(s);
        }

        function setSprintsCookie(sprints){
            $cookies.putObject('sprints', sprints);
            //$cookies.bySprint = JSON.stringify(sprints);
        }

        function isExistSprints(){
            return !!$cookies.getObject('sprints');
        }

        function getSprintsCookie(){
            if(!isExistSprints()) {
                return ;
            }

            return $cookies.getObject('sprints');//JSON.parse($cookies.bySprint);
        }

        function deleteSprintsCookie(){
            //delete $cookies.bySprint;
            $cookies.remove('sprints');
        }

    }
})();