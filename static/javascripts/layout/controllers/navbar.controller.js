/**
 * Created by lokolte on 08/05/15.
 */
/**
 * NavbarController
 * @namespace managers.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.layout.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', 'Authentication'];

    /**
     * @namespace NavbarController
     */
    function NavbarController($scope, Authentication) {
        var vm = this;

        vm.isAuthenticated = Authentication.isAuthenticated();

        vm.logout = logout;

        /**
         * @name logout
         * @desc Log the user out
         * @memberOf managers.layout.controllers.NavbarController
         */
        function logout() {
            Authentication.logout();
        }
    }
})();