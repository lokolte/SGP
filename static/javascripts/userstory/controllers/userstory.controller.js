/**
 * UserStoriesController controller
 * @namespace managers.userstory.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.userstory.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('UserStoriesController', UserStoriesController);

    UserStoriesController
        .$inject = ['$location', '$scope', '$cookies', 'Flujos', 'Proyectos', 'Actividades', 'Authentication', 'Sprints', 'HistorialUS'];

    /**
     * @namespace UserStoriesController
     */
    function UserStoriesController($location, $scope, $cookies, Flujos, Proyectos, Actividades, Authentication, Sprints, HistorialUS) {

        var vm = this;
        //variables
        vm.isExistProyectoSprint = false;

        vm.userstories = [];
        vm.userstory = {};
        vm.userstoryNulo = {};
        vm.estados = [];
        vm.hus = [];

        vm.flujos = [];
        vm.flujo = {};
        vm.flujoNulo = {};
        vm.proyecto = {};

        //funciones

        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;
        vm.definirEstado = definirEstado;
        vm.agregarEstado = agregarEstado;
        vm.agregarFlujo = agregarFlujo;
        vm.verHistorial = verHistorial;
        vm.agregarUS = agregarUS;

        activate();

        init();

        function init() {

            vm.isExistProyectoSprint = Sprints.isExistSprint() && Proyectos.isExistProyecto();

            if (vm.isExistProyectoSprint) {
                vm.proyecto = Proyectos.getProyectoCookie();
                vm.sprint = Sprints.getSprintCookie();
                console.log(vm.proyecto);
                console.log(vm.sprint);
                //console.log(Authentication.getAuthenticatedUsuario());
            }

            vm.estados = [
                {
                    'id': 1,
                    'estado': 'Pendiente'
                },
                {
                    'id': 2,
                    'estado': 'Suspendido'
                },
                {
                    'id': 3,
                    'estado': 'Finalizado'
                }
            ];
            //hacer el get para los flujos

            vm.userstoryNulo.nombre = '';
            vm.userstoryNulo.descripcionC = '';
            vm.userstoryNulo.estado = '';
            vm.userstoryNulo.tamanho = '';

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

            console.log('user story actual');
            console.log(vm.userstories);

            vm.flujos = [
                {
                    'index': 1,
                    'nombre': 'Analisis',
                    'estado': 'Doing',
                    'observacion': 'alguna observacion'
                },
                {
                    'index': 2,
                    'nombre': 'Desarrollo',
                    'estado': 'To_do',
                    'observacion': 'alguna observacion'
                }
            ];

            vm.flujoNulo.nombre = '';
            vm.flujoNulo.estado = '';
            vm.flujoNulo.observacion = '';

            if (!!$cookies.Sprints) {
                vm.sprints = JSON.parse($cookies.Sprints);
            } else {
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

                $cookies.Sprints = JSON.stringify(vm.sprints);
            }
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function guardar(/**/) {
            //Proyectos.create(/*datos del proyecto*/);
        }

        function cambiarEstado(/**/) {
            //Proyectos.cambiarEstado(/*datos del Estado*/);
        }

        function editar(userstory_in) {
            vm.userstory = userstory_in;
            definirEstado(userstory_in.estado);
            console.log('EL estado es: ' + vm.userstory.estado);
        }

        function clear() {
            vm.userstory = vm.userstoryNulo;
            vm.flujo = vm.flujoNulo;
        }

        function definirEstado(e) {
            if (e == 'Pendiente' || e == 'P') {
                vm.idEstado = vm.estados[0];
            } else if (e == 'Suspendido' || e == 'S') {
                vm.idEstado = vm.estados[1];
            } else if (e == 'Finalizado' || e == 'F') {
                vm.idEstado = vm.estados[2];
            }
        }

        function agregarEstado() {
            vm.userstory.estado = vm.estados[vm.idEstado - 1].estado;
            console.log(vm.userstory.estado);
        }

        function agregarFlujo() {
            vm.flujo = vm.flujos[vm.idFlujo - 1];
        }

        function verHistorial(us) {
            $cookies.USActual = JSON.stringify(us);
            $location.url('/historial');
        }

        function agregarUS(us) {
            var i = 0;
            for (i = 0; i < vm.sprints.length; i++) {
                if (vm.sprints[i].estado == 'Activo') {
                    vm.sprints[i].horasRest = vm.sprints[i].horasRest - us.tamanho;
                }
            }
            console.log(vm.sprints);
            $cookies.Sprints = JSON.stringify(vm.sprints);
            console.log(JSON.parse($cookies.Sprints));
            $location.url('/sprints');
        }
    }
})();