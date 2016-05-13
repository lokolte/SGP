/**
 * HistorialController controller
 * @namespace managers.historialus.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.historialus.controllers')
        .controller('HistorialController', HistorialController);

    HistorialController.$inject = ['$location', '$scope', '$cookies', 'Authentication', 'Kanbans', 'HistorialUS', 'UserStories'];

    /**
     * @namespace HistorialController
     */

    function HistorialController($location, $scope, $cookies, Authentication, Kanbans, HistorialUS, UserStories) {

        var vm = this;

        vm.historial = {};
        vm.historial.horas_trabajadas = 0;
        vm.historial.descripcion_trabajo = '';

        vm.historialuss = [];
        vm.hus = {};
        vm.hus.us = {};
        vm.hus.historial = [];

        vm.us = {};

        vm.volver = volver;

        activate();

        init();

        function init() {
            console.log('Empezamos el trabajo de ver historial');
            if (HistorialUS.isExistHistorial()) {
                vm.historialuss = HistorialUS.getHistorialCookie();
                console.log(vm.historialuss);
            }

            if (UserStories.isExistUS()) {
                vm.us = UserStories.getUSCookie();
                console.log(vm.us);
                if (HistorialUS.isExistHistorial()) {
                    var i = 0;
                    for (i = 0; i < vm.historialuss.length; i++) {
                        if (vm.historialuss[i].us.id == vm.us.id) {
                            vm.hus = vm.historialuss[i];
                            console.log('Historial actual');
                            console.log(vm.hus);
                            break;
                        }
                    }
                }

            }

        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function volver() {
            $location.url('/userstories');
        }
    }
})();