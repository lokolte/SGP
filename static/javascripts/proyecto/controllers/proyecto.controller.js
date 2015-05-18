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

        vm.dt_ini = new Date();
        vm.dt_fin = new Date();
        //vm.openedini = false;
        //vm.openedfin = false;

        vm.proyectos = [];

        vm.clientes = [];

        vm.proyecto = {};

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

        //vm.openini = openini;
        //vm.openfin = openfin;

        init();
        function init() {
            Proyectos.deleteProyectoCookie();

            vm.proyectos = [
                {
                    'nombre': 'Sistema de ventas',
                    'estado': 'Activo',
                    'fecha_ini': '2014-10-10',
                    'fecha_fin': '2015-10-10',
                    'observacion': 'alguna observacion'
                },
                {
                    'nombre': 'Sistema de compras',
                    'estado': 'Activo',
                    'fecha_ini': '2014-10-10',
                    'fecha_fin': '2015-10-10',
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
        }

        activate();

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

        function editar(proyecto_input) {
            vm.proyecto = proyecto_input;
            return vm.proyecto;
        }

        function clear(dt_ini) {
            dt_ini = new Date().setHours(0, 0, 0, 0);
            console.log(dt_ini);
        }

        function irFlujos(proyecto) {
            Proyectos.setProyectoCookie(proyecto);
            $location.url('/flujos');
            //JSON.stringify(usuario); convierte a algo para guardar
            //JSON.parse($cookies.authenticatedUsuario); transforma nuevamente a json
        }

        /*
         function openini($event) {
         $event.preventDefault();
         $event.stopPropagation();

         vm.openedini = true;
         }

         function openfin($event) {
         $event.preventDefault();
         $event.stopPropagation();

         vm.openedfin = true;
         }
         */
    }
})();