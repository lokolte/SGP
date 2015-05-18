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
        .$inject = ['$location', '$scope', 'Flujos', 'Proyectos', 'Actividades', 'Authentication', 'Sprints'];

    /**
     * @namespace UserStoriesController
     */
    function UserStoriesController($location, $scope, Flujos, Proyectos, Actividades, Authentication, Sprints) {

        var vm = this;
        //variables
        vm.isExistProyectoSprint = false;

        vm.userstories = [];
        vm.userstory = {};
        vm.userstoryNulo = {};
        vm.estados = [];

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

        activate();

        init();

        function init() {

            vm.isExistProyectoSprint = Sprints.isExistSprint() && Proyectos.isExistProyecto();

            if (vm.isExistProyectoSprint) {
                vm.proyecto = Proyectos.getProyectoCookie();
                vm.sprint = Sprints.getSprintCookie();
                console.log(vm.proyecto);
                console.log(vm.sprint);
                console.log(Authentication.getAuthenticatedUsuario());
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
            vm.userstories = [
                {
                    'nombre': 'Desarrollo Login backend',
                    'descripcionC': 'Dede ser Restful con djangorestframework',
                    'estado': 'Finalizado',
                    'tamanho': 5.00
                },
                {
                    'nombre': 'Desarrollo Login frontend',
                    'descripcionC': 'Dede ser con AngularJS',
                    'estado': 'Pendiente',
                    'tamanho': 4.00
                }
            ];

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

            vm.userstoryNulo.nombre = '';
            vm.userstoryNulo.descripcionC = '';
            vm.userstoryNulo.estado = '';
            vm.userstoryNulo.tamanho = '';

            vm.flujoNulo.nombre = '';
            vm.flujoNulo.estado = '';
            vm.flujoNulo.observacion = '';
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

        function agregarFlujo(){
            vm.flujo = vm.flujos[vm.idFlujo-1];
        }
    }
})();