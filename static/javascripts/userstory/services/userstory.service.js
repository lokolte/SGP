/**
 * UserStories
 * @namespace managers.userstory.services
 */
(function () {
    'use strict';

    angular
        .module('managers.userstory.services')
        .factory('UserStories', UserStories);

    UserStories.$inject = ['$http', '$cookies'];

    function UserStories($http, $cookies) {
        var UserStories = {
            all: all,
            create: create,
            get: get,
            modificar: modificar,

            setUSCookie: setUSCookie,
            getUSCookie: getUSCookie,
            isExistUS: isExistUS,
            deleteUSCookie: deleteUSCookie,

            setUSSCookie: setUSSCookie,
            getUSSCookie: getUSSCookie,
            isUSSCookie: isUSSCookie,
            deleteUSSCookie: deleteUSSCookie
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

        function setUSCookie(us){
            $cookies.putObject('UserStorie', us);
        }

        function isExistUS(){
            return !!$cookies.getObject('UserStorie');
        }

        function getUSCookie(){
            if(!isExistUS()) {
                return ;
            }

            return $cookies.getObject('UserStorie');
        }

        function deleteUSCookie(){
            $cookies.remove('UserStorie');
        }

        function setUSSCookie(uss){
             $cookies.putObject('UserStories', uss);
        }

        function isUSSCookie(){
             return !!$cookies.getObject('UserStories');
        }

        function getUSSCookie(){
             if(!isUSSCookie()){
                return ;
             }

            return $cookies.getObject('UserStories');
        }

        function deleteUSSCookie(){
            $cookies.remove('UserStories');
        }
    }
})();
