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
        vm.isEdit = false;
        vm.sprints = [];
        vm.sprint = {};
        vm.sprintNulo = {};

        vm.idEstado = {};
        vm.idEstado.e = {};
        vm.eNulo = {
            'id': 0,
            'estado': ''
        };
        vm.idEstado.e = vm.eNulo;

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
        vm.irSprintBl = irSprintBl;
        vm.irProductBl = irProductBl;

        activate();

        init();

        function init() {

            if (Proyectos.isExistProyecto()) {
                vm.proyecto = Proyectos.getProyectoCookie();
            }

            if (Sprints.isExistSprints()) {
                vm.sprints = Sprints.getSprintsCookie();
                console.log(vm.sprints);
                console.log('llego?');
            } else {
                vm.sprints = [
                    {
                        'lugar': 1,
                        'fecha_ini': devolverFechas(new Date(Date.parse('2015-05-20T00:38:30.656Z'))),
                        'duracionHoras': 20.00,
                        'estado': 'Cerrado',
                        'horasRest': 0.00
                    },
                    {
                        'lugar': 2,
                        'fecha_ini': devolverFechas(new Date(Date.parse('2015-05-12T00:38:30.656Z'))),
                        'duracionHoras': 20.00,
                        'estado': 'Activo',
                        'horasRest': 20.00
                    }
                ];
                //vm.sprints[0].fecha_ini = new Date(Date.parse(vm.sprints[0].fecha_ini));
                //vm.sprints[1].fecha_ini = new Date(Date.parse(vm.sprints[1].fecha_ini));

                Sprints.setSprintsCookie(vm.sprints);
                //$cookies.Sprints = JSON.stringify(vm.sprints);
            }

            console.log(vm.sprints);

            if (Sprints.isExistSprint()) {
                var s = Sprints.getSprintCookie();
                vm.sprints[s.lugar - 1] = s;
                Sprints.setSprintsCookie(vm.sprints);
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
            vm.sprints[vm.sprint.lugar - 1] = vm.sprint;
            vm.sprint = vm.sprintNulo;
            //Proyectos.create(/*datos del proyecto*/);
        }

        function cambiarEstado(/**/) {
            //Proyectos.cambiarEstado(/*datos del Estado*/);
        }

        function editar(sprint_input) {
            vm.sprint = sprint_input;
            vm.sprint.fecha_ini = new Date(Date.parse(vm.sprint.fecha_ini));
            console.log(sprint_input);
            definirEstado(sprint_input.estado);
            console.log('EL estado es: ' + vm.sprint.estado);
            vm.isEdit = true;
        }

        function clear() {
            vm.isEdit = false;
            vm.sprint = vm.sprintNulo;
            vm.idEstado.e = vm.eNulo;
        }

        function irUserStories(sprint) {
            Sprints.setSprintCookie(sprint);
            $location.url('/userstories');
        }

        function definirEstado(e) {
            if (e == 'Activo' || e == 'A') {
                vm.idEstado.e = vm.estados[0];
            } else if (e == 'Cerrado' || e == 'C') {
                vm.idEstado.e = vm.estados[1];
            }
        }

        function agregarEstado() {
            vm.sprint.estado = vm.estados[vm.idEstado.e.id - 1].estado;
            console.log(vm.sprint.estado);
        }

        function irSprintBl(s){
            Sprints.setSprintCookie(s);
            $location.url('/sprintbacklog');
        }

        function irProductBl(s){
            Sprints.setSprintCookie(s);
            $location.url('/productbacklog');
        }

        function devolverFechas(fecha){
            return fecha.toLocaleDateString();
        }

    }
})();