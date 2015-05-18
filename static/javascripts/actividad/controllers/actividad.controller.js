/**
 * ActividadesController controller
 * @namespace managers.actividad.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.flujo.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('ActividadesController', ActividadesController);

    ActividadesController
        .$inject = ['$location', '$scope', 'Flujos', 'Proyectos', 'Actividades', 'Authentication'];

    /**
     * @namespace ActividadesController
     */
    function ActividadesController($location, $scope, Flujos, Proyectos, Actividades, Authentication) {

        var vm = this;
        //variables
        vm.isExistProyectoFlujo = false;

        vm.actividades = [];
        vm.actividad = {};
        vm.actividadNula = {};
        vm.estados = [];

        vm.flujo = {};
        vm.proyecto = {};

        //funciones

        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;
        vm.definirEstado = definirEstado;
        vm.agregarEstado = agregarEstado;

        activate();

        init();

        function init() {

            vm.isExistProyectoFlujo = Flujos.isExistFlujo() && Proyectos.isExistProyecto();

            if (vm.isExistProyectoFlujo) {
                vm.proyecto = Proyectos.getProyectoCookie();
                vm.flujo = Flujos.getFlujoCookie();
                console.log(vm.proyecto);
                console.log(vm.flujo);
                console.log(Authentication.getAuthenticatedUsuario());
            }

            vm.estados = [
                {
                    'id': 1,
                    'estado': 'To_Do'
                },
                {
                    'id': 2,
                    'estado': 'Doing'
                },
                {
                    'id': 3,
                    'estado': 'Done'
                }
            ];
            //hacer el get para los flujos
            vm.actividades = [
                {
                    'nombre': 'Analisis',
                    'estado': 'Doing',
                    'orden': 1
                },
                {
                    'nombre': 'Desarrollo',
                    'estado': 'To_do',
                    'orden': 2
                }
            ];

            vm.actividadNula.nombre = '';
            vm.actividadNula.estado = '';
            vm.actividadNula.orden = '';
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

        function editar(actividad_in) {
            vm.actividad = actividad_in;
            definirEstado(actividad_in.estado);
            console.log('EL estado es: ' + vm.actividad.estado);
        }

        function clear() {
            vm.actividad = vm.actividadNula;
        }

        function definirEstado(e) {
            if (e == 'To_Do' || e == 'TD') {
                vm.idEstado = vm.estados[0];
            } else if (e == 'Doing' || e == 'DG') {
                vm.idEstado = vm.estados[1];
            } else if (e == 'Done' || e == 'DN') {
                vm.idEstado = vm.estados[2];
            }
        }

        function agregarEstado() {
            vm.actividad.estado = vm.estados[vm.idEstado - 1].estado;
            console.log(vm.actividad.estado);
        }
    }
})();