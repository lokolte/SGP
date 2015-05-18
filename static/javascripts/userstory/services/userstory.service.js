/**
 * UserStories
 * @namespace managers.userstory.services
 */
(function () {
    'use strict';

    angular
        .module('managers.userstory.services')
        .factory('UserStories', UserStories);

    UserStories.$inject = ['$http'];

    function UserStories($http) {
        var UserStories = {
            all: all,
            create: create,
            get: get,
            modificar: modificar
        };

        return UserStories;

        function all() {
            return $http.get('/api/userstories/');
        }

        function create(content) {
            return $http.post('/api/userstories/', {
                content: content
            });
        }

        function get(id) {
            return $http.get('/api/userstories/' + id);
        }

        function modificar(id) {
            return $http.put('/api/userstories/' + id);
        }
    }
})();
