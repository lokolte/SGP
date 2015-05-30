/**
 * HistorialController controller
 * @namespace managers.historialus.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.historialus.controllers')
        .controller('HistorialController', HistorialController);

    HistorialController.$inject = ['$location', '$scope', '$cookies', 'Authentication', 'Kanbans', 'HistorialUS'];

    /**
     * @namespace HistorialController
     */

    function HistorialController($location, $scope, $cookies, Authentication, Kanbans, HistorialUS) {

        var vm = this;

        vm.historialus = {};
        vm.usactual = {};
        vm.hus = [];

        vm.volver = volver;

        activate();

        init();

        function init() {

            if(HistorialUS.isExistHistorial()){
                vm.hus = HistorialUS.getHistorialCookie();
            }else{
                vm.hus=[{'horas_trabajas': 0, 'descripcion_trabajo': '', 'us': 0}, {'horas_trabajas': 0, 'descripcion_trabajo': '', 'us': 0}];
                HistorialUS.setHistorialCookie(vm.hus);
            }

            if(!!$cookies.USActual){
                vm.usactual=JSON.parse($cookies.USActual);
                console.log(vm.hus);
                console.log(vm.usactual);
                var i = 0;
                for(i=0; i<vm.hus.length; i++){
                    if(vm.hus[i].horas_trabajas==0){
                        vm.hus.splice(i,1);
                        console.log('elimino el cero?');
                        i=i-1;
                    }else if(vm.hus[i].us!=vm.usactual.fila){
                        vm.hus.splice(i,1);
                        console.log('elimino el que no es cero?');
                        i=i-1;
                    }
                }
                console.log(vm.hus);
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