/**
 * Created by lokolte on 16/05/15.
 */
/**
 * FlujosControllers controller
 * @namespace managers.flujo.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.flujo.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('FlujosControllers', FlujosControllers);

    FlujosControllers.$inject = ['$location', '$scope', 'Flujos', 'Proyectos', 'Authentication'];

    /**
     * @namespace FlujosControllers
     */
    function FlujosControllers($location, $scope, Flujos, Proyectos, Authentication) {

        var vm = this;

        vm.isExistProyecto = false;
        vm.flujos = [];
        vm.flujo = {};
        vm.proyecto = {};
        vm.estados = [];

        /**
         * valores del Json flujo
         * vm.flujo.nombre = '';
         * vm.flujo.estado = '';
         * vm.flujo.observacion = '';
         */

        init();

        function init() {

            vm.isExistProyecto = Proyectos.isExistProyecto();

            if (vm.isExistProyecto) {
                vm.proyecto = Proyectos.getProyectoCookie();
                console.log(vm.proyecto);
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
            vm.flujos = [
                {
                    'nombre': 'Analisis',
                    'estado': 'Doing',
                    'observacion': 'alguna observacion'
                },
                {
                    'nombre': 'Desarrollo',
                    'estado': 'To_do',
                    'observacion': 'alguna observacion'
                }
            ];
        }

        //vm.dt_ini = new Date();
        //vm.dt_fin = new Date();
        //vm.openedini = false;
        //vm.openedfin = false;

        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;
        vm.irActividades = irActividades;
        //vm.openini = openini;
        //vm.openfin = openfin;

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

        function editar(flujo_in) {
            vm.flujo = flujo_in;
        }

        function clear() {
            //vm.dt_ini = new Date();
            //return vm.dt_ini;
        }

        function irActividades(flujo){
            Flujos.setFlujoCookie(flujo);
            $location.url('/actividades');
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