/**
 * SprintsBLController controller
 * @namespace managers.sprint.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.sprint.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('SprintsBLController', SprintsBLController);

    SprintsBLController.$inject = ['$location', '$scope', '$cookies', 'Proyectos', 'Authentication', 'Sprints'];

    /**
     * @namespace SprintsBLController
     */
    function SprintsBLController($location, $scope, $cookies, Proyectos, Authentication, Sprints) {

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

        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }
    }
})();
