/**
 * HistorialUSController controller
 * @namespace managers.historialus.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.historialus.controllers')
        .controller('HistorialUSController', HistorialUSController);

    HistorialUSController.$inject = ['$location', '$scope', '$cookies', 'Authentication', 'Kanbans', 'HistorialUS', 'UserStories'];

    /**
     * @namespace HistorialUSController
     */

    function HistorialUSController($location, $scope, $cookies, Authentication, Kanbans, HistorialUS, UserStories) {

        var vm = this;

        vm.historial = {};
        vm.historial.horas_trabajadas = 0;
        vm.historial.descripcion_trabajo = '';

        vm.userstories = [];
        vm.i = 0;
        vm.encontrado = false;

        vm.historialuss = [];
        vm.hus = {};
        vm.hus.us = {};
        vm.hus.historial = [];

        vm.us = {};
        vm.usnulo = {};

        vm.guardar = guardar;

        activate();

        init();

        function init() {

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

            if (UserStories.isUSSCookie) {
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

            if (HistorialUS.isExistHistorial()) {
                vm.historialuss = HistorialUS.getHistorialCookie();
                console.log('trajo el Historial?');
                console.log(vm.historialuss);
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

            if (UserStories.isExistUS()) {
                vm.us = UserStories.getUSCookie();
            }
            console.log('User Storie Actual es: ')
            console.log(vm.us);
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function guardar() {
            console.log('Entro1');
            vm.us.tamanho = vm.us.tamanho - vm.historial.horas_trabajadas;
            console.log(vm.historial.horas_trabajadas);
            console.log('Entro2');
            vm.i = -1;
            vm.i = conseguirUS(vm.us);
            console.log(vm.i);
            console.log('Entro3');
            if (vm.i != -1) {
                vm.userstories[vm.i] = vm.us;
                UserStories.setUSSCookie(vm.userstories);
                console.log('UserStories actual es: ');
                console.log(UserStories.getUSSCookie());
            }
            console.log('Entro4 con historialuss: ');
            console.log(vm.historialuss);

            if (vm.historialuss.length!=0) {
                console.log('Entra para agregar a Huss');
                console.log(vm.historialuss);
                console.log('user story');
                console.log(vm.us);
                var j = 0;
                for (j = 0; j < vm.historialuss.length; j++) {
                    if (vm.historialuss[j].us.id == vm.us.id) {
                        vm.historialuss[j].historial.push(vm.historial);
                        HistorialUS.setHistorialCookie(vm.historialuss);
                        vm.encontrado = true;
                    }
                }
            }

            if (!vm.encontrado && vm.us.id!=0) {
                vm.hus.us = vm.us;
                console.log(vm.hus);
                vm.hus.historial.push(vm.historial);
                console.log(vm.hus);
                vm.historialuss.push(vm.hus);
                console.log('Veamos los Us');
                console.log(vm.historialuss);
                HistorialUS.setHistorialCookie(vm.historialuss);
            }
            console.log('Verificando si guardo');
            console.log(HistorialUS.getHistorialCookie());
            //HistorialUS.setHistorialCookie('si guardo');
            console.log(HistorialUS.getHistorialCookie());
            console.log(HistorialUS.getHistorialCookie());
            console.log(HistorialUS.getHistorialCookie());

            $location.url('/userstories');
        }

        function conseguirUS(us) {
            var j = 0;
            for (j = 0; j < vm.userstories.length; j++) {
                if (us.id == vm.userstories[j].id) {
                    return j;
                }
            }
            return vm.usnulo;
        }
    }
})();