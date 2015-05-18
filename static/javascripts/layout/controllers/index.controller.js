/**
 * Created by lokolte on 10/05/15.
 */
/**
 * IndexController
 *
 * @namespace managers.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', '$location', 'Authentication', 'Snackbar'];

    /**
     * @namespace IndexController
     */
    function IndexController($scope, $location, Authentication, Snackbar) {
        var vm = this;

        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf managers.layout.controllers.IndexController
         */
        function activate() {

            // If the user is authenticated, they should not be here.
            if (Authentication.isAuthenticated()) {
                //Snackbar.error('Usuario logueado!!');
                //$location.url('/');
            }

        }
    }
})();