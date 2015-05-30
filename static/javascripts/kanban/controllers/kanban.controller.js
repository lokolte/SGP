/**
 * KanbansController controller
 * @namespace managers.kanban.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.kanban.controllers')
        .controller('KanbansController', KanbansController);

    KanbansController.$inject = ['$location', '$scope', '$cookies', 'Proyectos', 'Authentication', 'Kanbans'];

    /**
     * @namespace KanbansController
     */
    function KanbansController($location, $scope, $cookies, Proyectos, Authentication, Kanbans) {

        var vm = this;

        vm.userstories = [];

        vm.kanbanus = [];
        vm.item = {};

        vm.flujo = {};
        vm.us = {};
        vm.userstories = [];
        vm.usnulo = {};

        vm.avanzar = avanzar;
        vm.retrasar = retrasar;
        vm.registrarTrabajo = registrarTrabajo;
        //vm.irHistorial = irHistorial;

        activate();

        init();

        function init() {

            vm.usnulo.nombre = '';
            vm.usnulo.descripcionC = '';
            vm.usnulo.estado = '';
            vm.usnulo.tamanho = '';

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

            vm.kanbanus = [
                {
                    'analisis': {},
                    'disenho': {}
                },
                {
                    'analisis': {},
                    'disenho': {}
                }
            ];

            vm.kanbanus[0].analisis=vm.userstories[0];
            vm.kanbanus[0].disenho=vm.usnulo;

            vm.kanbanus[1].analisis=vm.usnulo;
            vm.kanbanus[1].disenho=vm.userstories[1];

            console.log(vm.kanbanus);
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function avanzar(us){
            if(us.analisis.nombre!=''){
                us.disenho=us.analisis;
                us.analisis=vm.usnulo;
            }
        }

        function retrasar(us){
            if(us.disenho.nombre!=''){
                us.analisis=us.disenho;
                us.disenho=vm.usnulo;
            }
        }

        function registrarTrabajo(us){
            Kanbans.setkanbanCookie(us);
            $location.url('/historialus');
        }
    }
})();