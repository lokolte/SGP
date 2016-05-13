(function () {
    'use strict';

    angular
        .module('managers.bordownchart.controllers')
        .controller('bordownchartController', bordownchartController);

    bordownchartController.$inject = ['$location', '$scope', 'Proyectos'];

    function bordownchartController($location, $scope, Proyectos) {
        var vm = this;

        vm.horasus = [];
        vm.dias = [];
        vm.series = [];

        vm.proyecto = {};//proyecto actual

        vm.respon = {};//aqui se guardan los datos de las respuestas

        vm.historialuss = [];
        vm.hus = {};
        vm.hus.us = {};
        vm.hus.historial = [];

        //vm.init = init;
        vm.accion = accion;

        function accion(points, evt) {
            //console.log(points[0].value, evt);
            console.log('hacer algo!!');
        }

        init();

        function init() {
            console.log('Llego a entrar al controller?');
            vm.proyecto = Proyectos.getProyectoCookie();
            vm.series = ['Trabajo Real', 'Trabajo Estimado'];
            if (vm.proyecto.id == 2) {
                //ejecutar aqui el http.get para los datos del array
                vm.respon = {
                    "dias": ["1 dia", "2 dia", "3 dia", "4 dia", "5 dia", "6 dia", "7 dia", "8 dia",
                        "9 dia", "10 dia", "11 dia", "12 dia", "13 dia", "14 dia", "15 dia", "16 dia",
                        "17 dia", "18 dia", "19 dia", "20 dia", "21 dia", "22 dia", "23 dia", "24 dia",
                        "25 dia", "26 dia", "27 dia", "28 dia"],
                    "horas": [
                        [5, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        /*[8, 7, 7, 7, 6, 6, 6, 5, 5, 5,
                            5, 4, 4, 4, 3, 3, 3, 3, 2, 2,
                            2, 1, 1, 1, 1, 0, 0, 0]*/

                        [8, 7.71, 7.42, 7.13, 6.84, 6.55, 6.26, 5.97, 5.68, 5.39,
                            5.1, 4.81, 4.52, 4.23, 3.94, 3.65, 3.36, 3.07, 2.78, 2.49,
                            2.2, 1.91, 1.62, 1.33, 1.04, 0.75, 0.46, 0.17]
                    ]
                };
                vm.horasus = vm.respon.horas;
                vm.dias = vm.respon.dias;
            }else if(vm.proyecto.id == 1){
                 vm.respon = {
                    "dias": ["1 dia", "2 dia", "3 dia"],
                    "horas": [
                        [5, 3, 1],
                        //[8, 5, 2]
                        [8, 5.33, 2.66]
                    ]
                };
                vm.horasus = vm.respon.horas;
                vm.dias = vm.respon.dias;
            }
        }
    }
})();