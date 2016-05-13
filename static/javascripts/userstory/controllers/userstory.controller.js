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
        .$inject = ['$location', '$scope', '$cookies', 'Flujos', 'Proyectos', 'Actividades', 'Authentication', 'Sprints', 'HistorialUS', 'UserStories'];

    /**
     * @namespace UserStoriesController
     */
    function UserStoriesController($location, $scope, $cookies, Flujos, Proyectos, Actividades, Authentication, Sprints, HistorialUS, UserStories) {

        var vm = this;
        //variables
        vm.isExistProyectoSprint = false;

        vm.userstories = [];
        vm.userstory = {};
        vm.usnulo = {};
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

            vm.usnulo = {
                'nombre': '',
                'descripcionC': '',
                'estado': '',
                'tamanho': 0,
                'fila': 0,
                'Actividad': {
                    'nombre': '',
                    'estado': '',
                    'orden': 0
                }
            };

            if (UserStories.isUSSCookie()) {
                vm.userstories = UserStories.getUSSCookie();
            } else {
                vm.userstories = [
                    {
                        'id': 1,
                        'nombre': 'Desarrollo Login frontend',
                        'descripcionC': 'Dede ser con AngularJS',
                        'estado': 'Pendiente',
                        'tamanho': 4.00,
                        'fila': 2,
                        'Actividad': {
                            'nombre': 'Analisis',
                            'estado': 'Doing',
                            'orden': 1
                        }
                    },
                    {
                        'id': 2,
                        'nombre': 'Desarrollo Login backend',
                        'descripcionC': 'Dede ser Restful con djangorestframework',
                        'estado': 'Finalizado',
                        'tamanho': 5.00,
                        'fila': 1,
                        'Actividad': {
                            'nombre': 'Desarrollo',
                            'estado': 'To_do',
                            'orden': 2
                        }
                    }
                ];

                UserStories.setUSSCookie(vm.userstories);
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

            if (Sprints.isExistSprints()) {
                vm.sprints = Sprints.getSprintsCookie();
                console.log(vm.sprints);
                console.log('leyo los sprints?');
            } else {
                vm.sprints = [
                    {
                        'lugar': 1,
                        'fecha_ini': '2015-05-20T00:38:30.656Z',
                        'duracionHoras': 20.00,
                        'estado': 'Cerrado',
                        'horasRest': 0.00
                    },
                    {
                        'lugar': 2,
                        'fecha_ini': new Date(Date.parse('2015-05-12T00:38:30.656Z')),
                        'duracionHoras': 20.00,
                        'estado': 'Activo',
                        'horasRest': 20.00
                    }
                ];

                Sprints.setSprintsCookie(vm.sprints);
                //$cookies.Sprints = JSON.stringify(vm.sprints);
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
            vm.userstory = vm.usnulo;
            vm.flujo = vm.flujoNulo;
        }

        function definirEstado(e) {

            if (e == 'Pendiente' || e == 'P') {
                if (e == 'Activo' || e == 'A') {
                    vm.idEstado.e = vm.estados[0];
                } else if (e == 'Suspendido' || e == 'S') {
                    vm.idEstado.e = vm.estados[1];
                } else if (e == 'Finalizado' || e == 'F') {
                    vm.idEstado.e = vm.estados[2];
                }
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
            UserStories.setUSCookie(us);
            $location.url('/historial');
        }

        function agregarUS(us) {
            var i = 0;
            for (i = 0; i < vm.sprints.length; i++) {
                if (vm.sprints[i].estado == 'Activo') {
                    vm.sprints[i].horasRest = vm.sprints[i].horasRest - us.tamanho;
                }
            }
            console.log('Analizando los Sprints');
            console.log(vm.sprints);
            Sprints.deleteSprintsCookie();
            Sprints.setSprintsCookie(vm.sprints);//$cookies.Sprints = JSON.stringify(vm.sprints);
            console.log(Sprints.getSprintsCookie());
            $location.url('/sprints');
        }
    }

})();