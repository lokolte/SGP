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
        .controller('FlujosController', FlujosController);

    FlujosController.$inject = ['$location', '$scope', 'Flujos', 'Proyectos', 'Authentication'];

    /**
     * @namespace FlujosControllers
     */
    function FlujosController($location, $scope, Flujos, Proyectos, Authentication) {

        var vm = this;

        //variables
        vm.isExistProyecto = false;

        vm.flujos = [];
        vm.flujo = {};
        vm.flujoNulo = {};

        vm.proyecto = {};
        vm.estados = [];

        /**
         * valores del Json flujo
         * vm.flujo.nombre = '';
         * vm.flujo.estado = '';
         * vm.flujo.observacion = '';
         */

        //funciones
        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;

        vm.irActividades = irActividades;
        vm.definirEstado = definirEstado;
        vm.agregarEstado = agregarEstado;

        init();

        function init() {

            Flujos.deleteFlujoCookie();

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
            //hacer el get para los flujos con vm.proyecto
            vm.flujos = [
                {
                    'nombre': 'Analisis',
                    'estado': 'Doing',
                    'observacion': 'alguna observacion'
                },
                {
                    'nombre': 'Desarrollo',
                    'estado': 'To_Do',
                    'observacion': 'alguna observacion'
                }
            ];
            vm.flujoNulo.nombre = '';
            vm.flujoNulo.estado = '';
            vm.flujoNulo.observacion = '';
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

        function editar(flujo_in) {
            vm.flujo = flujo_in;
            definirEstado(flujo_in.estado);
            console.log('EL estado es: ' + vm.flujo.estado);
        }

        function clear() {
            vm.flujo=vm.flujoNulo;
        }

        function irActividades(flujo){
            Flujos.setFlujoCookie(flujo);
            $location.url('/actividades');
        }

        function definirEstado(e){
            if(e == 'To_Do' || e == 'TD'){
                vm.idEstado = vm.estados[0];
            }else if(e == 'Doing' || e == 'DG'){
                vm.idEstado = vm.estados[1];
            }else if(e == 'Done' || e == 'DN'){
                vm.idEstado = vm.estados[2];
            }
        }

        function agregarEstado(){
            vm.flujo.estado = vm.estados[vm.idEstado-1].estado;
            console.log(vm.flujo.estado);
        }
    }
})();