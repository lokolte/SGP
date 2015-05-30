/**
 * SprintsController controller
 * @namespace managers.sprint.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.sprint.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('SprintsController', SprintsController);

    SprintsController.$inject = ['$location', '$scope', '$cookies', 'Proyectos', 'Authentication', 'Sprints'];

    /**
     * @namespace SprintsController
     */
    function SprintsController($location, $scope, $cookies, Proyectos, Authentication, Sprints) {

        var vm = this;

        //variables
        vm.sprints = [];
        vm.sprint = {};
        vm.sprintNulo = {};

        vm.proyecto = {};

        vm.userstories = [];

        //funciones

        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;
        vm.definirEstado = definirEstado;
        vm.agregarEstado = agregarEstado;
        vm.irUserStories = irUserStories;

        activate();

        init();

        function init() {

            if(Proyectos.isExistProyecto()){
                vm.proyecto = Proyectos.getProyectoCookie();
            }

            vm.sprints = [
                {
                    'lugar': 1,
                    'fecha_ini': new Date(),
                    'duracionHoras': 20.00,
                    'estado': 'Cerrado',
                    'horasRest': 0.00
                },
                {
                    'lugar': 2,
                    'fecha_ini': new Date(),
                    'duracionHoras': 20.00,
                    'estado': 'Activo',
                    'horasRest': 20.00
                }
            ];

            if(!$cookies.Sprints){
                $cookies.Sprints = JSON.stringify(vm.sprints);
            }else{
                vm.sprints=JSON.parse($cookies.Sprints);
            }

            if(Sprints.isExistSprint()){
                var s = Sprints.getSprintCookie();
                vm.sprints[s.lugar-1] = s;
            }

            vm.estados = [
                {
                    'id': 1,
                    'estado': 'Activo'
                },
                {
                    'id': 2,
                    'estado': 'Cerrado'
                }
            ];

            //inicializando un proyecto nulo
            vm.sprintNulo.lugar = '';
            vm.sprintNulo.fecha_ini = new Date();
            vm.sprintNulo.duracionHoras = '';
            vm.sprintNulo.estado = '';
            vm.sprintNulo.horasRest = '';

            vm.sprint = vm.sprintNulo;
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function guardar(/**/) {
            vm.sprints.push(vm.sprint);
            vm.sprint = vm.sprintNulo;
            //Proyectos.create(/*datos del proyecto*/);
        }

        function cambiarEstado(/**/) {
            //Proyectos.cambiarEstado(/*datos del Estado*/);
        }

        function editar(sprint_input) {
            vm.sprint = sprint_input;
            definirEstado(sprint_input.estado);
            console.log('EL estado es: ' + vm.sprint.estado);
        }

        function clear() {
            vm.sprint = vm.sprintNulo;
        }

        function irUserStories(sprint) {
            Sprints.setSprintCookie(sprint);
            $location.url('/userstories');
        }

        function definirEstado(e) {
            if (e == 'Activo' || e == 'A') {
                vm.idEstado = vm.estados[0];
            } else if (e == 'Cerrado' || e == 'C') {
                vm.idEstado = vm.estados[1];
            }
        }

        function agregarEstado() {
            vm.sprint.estado = vm.estados[vm.idEstado - 1].estado;
            console.log(vm.sprint.estado);
        }

    }
})();