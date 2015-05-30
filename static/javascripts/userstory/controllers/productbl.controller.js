/**
 * ProductBLController controller
 * @namespace managers.userstory.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.userstory.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('ProductBLController', ProductBLController);

    ProductBLController.$inject = ['$location', '$scope', '$cookies', 'Proyectos', 'Authentication', 'Sprints'];

    /**
     * @namespace ProductBLController
     */
    function ProductBLController($location, $scope, $cookies, Proyectos, Authentication, Sprints) {

        var vm = this;

        //variables
        vm.sprint = {};

        vm.proyecto = {};

        vm.userstories = [];

        //funciones

        activate();

        init();

        function init() {

            if(Proyectos.isExistProyecto()){
                vm.proyecto = Proyectos.getProyectoCookie();
            }

            if(!!$cookies.Sprintbl){
                vm.sprint = JSON.parse($cookies.Sprintbl);
            }

            if (!!$cookies.UserStories) {
                vm.userstories = JSON.parse($cookies.UserStories);
            } else {
                vm.userstories = [
                    {
                        'nombre': 'Desarrollo Login backend',
                        'descripcionC': 'Dede ser Restful con djangorestframework',
                        'estado': 'Finalizado',
                        'tamanho': 5.00,
                        'fila': 1
                    },
                    {
                        'nombre': 'Desarrollo Login frontend',
                        'descripcionC': 'Dede ser con AngularJS',
                        'estado': 'Pendiente',
                        'tamanho': 4.00,
                        'fila': 2
                    }
                ];
                $cookies.UserStories = JSON.stringify(vm.userstories);
            }
            var i = 0;
            for(i=0; i<vm.userstories.length; i++){
                console.log(vm.userstories[i].estado);
                if(vm.userstories[i].estado!='Pendiente'){
                    vm.userstories.splice(i,1);
                }
            }
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }
    }
})();

