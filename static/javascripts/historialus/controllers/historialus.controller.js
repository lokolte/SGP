/**
 * HistorialUSController controller
 * @namespace managers.historialus.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.historialus.controllers')
        .controller('HistorialUSController', HistorialUSController);

    HistorialUSController.$inject = ['$location', '$scope', '$cookies', 'Authentication', 'Kanbans', 'HistorialUS'];

    /**
     * @namespace HistorialUSController
     */

    function HistorialUSController($location, $scope, $cookies, Authentication, Kanbans, HistorialUS) {

        var vm = this;

        vm.userstories = [];
        vm.historialus = {};
        vm.hus = [];

        vm.us = {};
        vm.usnulo = {};

        vm.guardar = guardar;

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

            if(!HistorialUS.isExistHistorial()){
                vm.hus = HistorialUS.getHistorialCookie();
            }else{
                vm.hus=[{'horas_trabajas': 0, 'descripcion_trabajo': '', 'us': 0}, {'horas_trabajas': 0, 'descripcion_trabajo': '', 'us': 0}];
                HistorialUS.setHistorialCookie(vm.hus);
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

            if(Kanbans.isExistkanban()){
                console.log('Encontro el kanban?');
                vm.us = Kanbans.getkanbanCookie();
                if(vm.us.disenho.nombre!=''){
                    vm.us=vm.us.disenho;
                    vm.historialus.us=vm.us.fila;
                }else{
                    vm.us=vm.us.analisis;
                    vm.historialus.us=vm.us.fila;
                }
            }

            console.log(vm.us);

        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function guardar() {
            vm.us.tamanho = vm.us.tamanho - vm.historialus.horas_trabajas;

            if(vm.us.fila==1){
                vm.userstories[0]=vm.us;
            }else{
                vm.userstories[1]=vm.us;
            }

            $cookies.UserStories = JSON.stringify(vm.userstories);

            if(vm.hus[0].horas_trabajas==0){
                vm.hus[0]=vm.historialus;
            }else if(vm.hus[1].horas_trabajas==0) {
                vm.hus[1]=vm.historialus;
            }else{
                vm.hus.push(vm.historialus);
            }

            HistorialUS.setHistorialCookie(vm.hus);

            console.log(vm.hus);

            $location.url('/userstories');
        }
    }
})();