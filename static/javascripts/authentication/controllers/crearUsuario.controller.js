/**
 * Created by Jesus Aguilar on 27/03/2015.
 */
/**
 * CrearUsuario controller
 * @namespace managers.authentication.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.authentication.controllers')
        .controller('crearUsuarioController', crearUsuarioController);

    crearUsuarioController.$inject = ['$location', '$scope', 'Authentication'];

    /**
     * @namespace crearusuarioController
     */
    function crearUsuarioController($location, $scope, Authentication) {
        var vm = this;

        vm.register = register;

        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf managers.authentication.controllers.crearUsuarioController
         */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }

        /**
         * @name crearusuarioController
         * @desc Register a new user
         * @memberOf managers.authentication.controllers.crearUsuarioController
         */

        function register() {
            Authentication.register(vm.username, vm.password, vm.email, vm.nombre, vm.apellido);
        }
    }
})();