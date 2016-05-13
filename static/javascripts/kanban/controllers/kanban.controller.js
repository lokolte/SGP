/**
 * KanbansController controller
 * @namespace managers.kanban.controllers
 */
(function () {
    'use strict';

    angular
        .module('managers.kanban.controllers')
        .controller('KanbansController', KanbansController);

    KanbansController.$inject = ['$location', '$scope', '$cookies', 'Proyectos', 'Authentication', 'Kanbans', 'UserStories', 'Actividades', 'Flujos'];

    /**
     * @namespace KanbansController
     */
    function KanbansController($location, $scope, $cookies, Proyectos, Authentication, Kanbans, UserStories, Actividades, Flujos) {

        var vm = this;

        vm.userstories = [];
        vm.actividades = [];
        vm.estados = [];

        vm.kanbanus = [];

        vm.flujo = {};
        vm.us = {};
        vm.usnulo = {};

        vm.avanzar = avanzar;
        vm.retrasar = retrasar;
        vm.registrarTrabajo = registrarTrabajo;
        vm.isVisualize = isVisualize;
        //vm.irHistorial = irHistorial;

        activate();

        init();

        function init() {

            if(Flujos.isExistFlujo()){
                vm.flujo = Flujos.getFlujoCookie();
                console.log(vm.flujo);
            }

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

            vm.estados = [
                {
                    'id': 1,
                    'estado': 'Pendiente',
                    'key': 'P'
                },
                {
                    'id': 2,
                    'estado': 'Suspendido',
                    'key': 'S'
                },
                {
                    'id': 3,
                    'estado': 'Finalizado',
                    'key': 'F'
                }
            ];

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
            /*if (!Actividades.isActividadesCookie()) {
                vm.actividades = Actividades.getActividadesCookie();
            } else {*/
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
                    },
                    {
                        'nombre': 'Implementacion',
                        'estado': 'To_do',
                        'orden': 3
                    }
                ];

                Actividades.setActividadesCookie(vm.actividades);
            //}
            //aqui se deben traer los US de un flujo dado y armar el ARRAY del kamban
            //a partir del orden de su actividad
            vm.kanbanus = crearKamban(vm.userstories, vm.actividades.length, vm.usnulo);

            console.log(vm.kanbanus);
        }

        /*
         * Para crear el kamban es necesario un array de las actividades
         * y el array de los UserStories existentes del flujo dado
         * */
        function crearKamban(uss, cant_actividades, usnulo) {
            console.log(uss);
            var cant_us = uss.length;
            var kb = new Array(cant_us);

            var i = 0;
            for (i = 0; i < cant_us; i++) {
                kb[i] = new Array(cant_actividades);
            }

            var i = 0;
            for (i = 0; i < cant_us; i++) {
                var j = 0;
                for (j = 0; j < cant_actividades; j++) {
                    kb[i][j] = usnulo;
                }
            }

            var i = 0;
            var orden = 1;
            while (orden <= cant_actividades) {
                console.log(orden);
                for (i = 0; i < cant_us; i++) {
                    if (uss[i].Actividad.orden == orden) {
                        kb[i][orden - 1] = uss[i];
                    }
                }
                orden++;
            }

            return kb;
        }

        function activate() {
            // If the user is authenticated, they should not be here.
            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }
        }

        function conseguirUS(line) {
            var cant_actvidades = vm.actividades.length;
            var j = 0;
            for (j = 0; j < cant_actvidades; j++) {
                if (line[j] != vm.usnulo) {
                    return line[j];
                }
            }
        }

        function avanzar(lineus) {
            console.log(lineus);
            var u = conseguirUS(lineus);
            var i = 0;

            console.log('entro verifiquemos los us');
            console.log(u);

            for (i = 0; i < vm.userstories.length; i++) {

                if (u.id == vm.userstories[i].id) {

                    if (vm.userstories[i].estado != 'Finalizado') {

                        if (vm.userstories[i].estado == 'Pendiente') {
                            vm.userstories[i].estado = 'Finalizado';

                        } else if (vm.userstories[i].estado == 'Suspendido') {
                            vm.userstories[i].estado = 'Pendiente';

                        }

                    } else if (vm.userstories[i].estado == 'Finalizado') {
                        if (vm.userstories[i].Actividad.orden + 1 <= vm.actividades.length) {
                            vm.userstories[i].Actividad = vm.actividades[vm.userstories[i].Actividad.orden];
                            vm.userstories[i].estado = 'Pendiente';
                        }
                    }
                }
            }
            //enviar cambios al backend
            vm.kanbanus = crearKamban(vm.userstories, vm.actividades.length, vm.usnulo);
        }

        function isVisualize(index) {
            console.log('indice: ' + index);

            return (index + 1) == vm.actividades.length;
        }

        function retrasar(lineus) {
            console.log(lineus);
            var u = conseguirUS(lineus);
            var i = 0;

            console.log('entro verifiquemos los us');
            console.log(u);

            for (i = 0; i < vm.userstories.length; i++) {

                if (u.id == vm.userstories[i].id) {

                    if (vm.userstories[i].estado != 'Suspendido') {

                        if (vm.userstories[i].estado == 'Pendiente') {
                            vm.userstories[i].estado = 'Suspendido';

                        } else if (vm.userstories[i].estado == 'Finalizado') {
                            vm.userstories[i].estado = 'Pendiente';

                        }

                    } else if (vm.userstories[i].estado == 'Suspendido') {
                        if (vm.userstories[i].Actividad.orden - 1 > 0) {
                            vm.userstories[i].Actividad = vm.actividades[vm.userstories[i].Actividad.orden - 2];
                            vm.userstories[i].estado = 'Pendiente';
                        }
                    }
                }
            }
            //enviar cambios al backend
            vm.kanbanus = crearKamban(vm.userstories, vm.actividades.length, vm.usnulo);
        }

        function registrarTrabajo(lineus) {
            var us = conseguirUS(lineus);
            Kanbans.setkanbanCookie(vm.kanbanus);
            UserStories.setUSCookie(us);
            console.log(UserStories.getUSCookie());
            $location.url('/historialus');
        }
    }
})
();