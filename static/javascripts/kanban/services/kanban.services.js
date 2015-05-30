/**
 * Kanbans
 * @namespace managers.kanban.services
 */
(function () {
    'use strict';

    angular
        .module('managers.kanban.services')
        .factory('Kanbans', Kanbans);

    Kanbans.$inject = ['$http', '$cookies'];

    function Kanbans($http, $cookies) {

        var Kanbans = {
            setkanbanCookie: setkanbanCookie,
            getkanbanCookie: getkanbanCookie,
            isExistkanban: isExistkanban,
            deletekanbanCookie: deletekanbanCookie
        };

        return Kanbans;

        function setkanbanCookie(kanban){
            $cookies.byKanban = JSON.stringify(kanban);
        }

        function isExistkanban(){
            return !!$cookies.byKanban;
        }

        function getkanbanCookie(){
            if(!isExistkanban()) {
                return ;
            }

            return JSON.parse($cookies.byKanban);
        }

        function deletekanbanCookie(){
            delete $cookies.byKanban;
        }

    }
})();