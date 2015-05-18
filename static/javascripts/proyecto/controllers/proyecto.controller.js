/**
 * ProyectosController controller
 * @namespace managers.proyecto.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.proyecto.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('ProyectosController', ProyectosController);

    ProyectosController.$inject = ['$location', '$scope', 'Proyectos', 'Authentication'];

    /**
     * @namespace ProyectosController
     */
    function ProyectosController($location, $scope, Proyectos, Authentication) {

        var vm = this;

        //vm.openedini = false;
        //vm.openedfin = false;

        vm.proyectos = [];
        vm.proyecto = {};
        vm.proyectoNulo = {};

        vm.clientes = [];


        /**
         *Datos del proyecto
         * vm.proyecto.nombre = '';
         * vm.proyecto.estado = '';
         * vm.proyecto.fecha_ini = '';
         * vm.proyecto.fecha_fin = '';
         * vm.proyecto.observacion = '';
         */

        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;
        vm.irFlujos = irFlujos;
        vm.definirEstado = definirEstado;
        vm.agregarEstado = agregarEstado;
        vm.irSprint = irSprint;

        //vm.openini = openini;
        //vm.openfin = openfin;

        activate();

        init();

        function init() {
            Proyectos.deleteProyectoCookie();

            vm.proyectos = [
                {
                    'nombre': 'Sistema de ventas',
                    'estado': 'Activo',
                    'fecha_ini': new Date(),
                    'fecha_fin': new Date(),
                    'observacion': 'alguna observacion'
                },
                {
                    'nombre': 'Sistema de compras',
                    'estado': 'Activo',
                    'fecha_ini': new Date(),
                    'fecha_fin': new Date(),
                    'observacion': 'alguna observacion'
                }
            ];

            vm.estados = [
                {
                    'id': 1,
                    'estado': 'Activo'
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

            //inicializando un proyecto nulo
            vm.proyectoNulo.nombre = '';
            vm.proyectoNulo.estado = '';
            vm.proyectoNulo.fecha_ini = new Date();
            vm.proyectoNulo.fecha_fin = new Date();
            vm.proyectoNulo.observacion = '';

            vm.proyecto = vm.proyectoNulo;

            console.log(new Date());
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function guardar(/**/) {
            vm.proyectos.push(vm.proyecto);
            vm.proyecto = vm.proyectoNulo;
            //Proyectos.create(/*datos del proyecto*/);
        }

        function cambiarEstado(/**/) {
            //Proyectos.cambiarEstado(/*datos del Estado*/);
        }

        function editar(proyecto_input) {
            vm.proyecto = proyecto_input;
            definirEstado(proyecto_input.estado);
            console.log('EL estado es: ' + vm.proyecto.estado);
        }

        function clear() {
            vm.proyecto = vm.proyectoNulo;
        }

        function irFlujos(proyecto) {
            Proyectos.setProyectoCookie(proyecto);
            $location.url('/flujos');
        }

        function definirEstado(e){
            if(e == 'Activo' || e == 'A'){
                vm.idEstado = vm.estados[0];
            }else if(e == 'Suspendido' || e == 'S'){
                vm.idEstado = vm.estados[1];
            }else if(e == 'Finalizado' || e == 'F'){
                vm.idEstado = vm.estados[2];
            }
        }

        function agregarEstado(){
            vm.proyecto.estado = vm.estados[vm.idEstado-1].estado;
            console.log(vm.proyecto.estado);
        }

        function irSprint(proyecto){
            Proyectos.setProyectoCookie(proyecto);
            $location.url('/sprints');
        }
    }
})();