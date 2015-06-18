(function () {
    'use strict';

    angular
        .module('managers.table.controllers')
        .controller('TableController', TableController);

    TableController.$inject = ['$scope', '$filter', '$http'];

    function TableController($scope, $http) {
        var vm = this;
        vm.data = [];
        vm.dias = [];
        vm.series = ['Sprint Real', 'Sprint Estimado'];

        vm.proyecto = {};//proyecto actual

        vm.respon = {};//aqui se guardan los datos de las respuestas

        vm.init = init;
        vm.accion = accion;

        function accion(points, evt) {
            console.log(points[0].value, evt);
            console.log('hacer algo!!');
        };

        function init() {
            //ejecutar aqui el http.get para los datos del array
            vm.respon = {
                "dias": ["1 dia", "2 dia", "3 dia", "4 dia", "5 dia", "6 dia", "7 dia", "8 dia",
                    "9 dia", "10 dia", "11 dia", "12 dia", "13 dia", "14 dia", "15 dia", "16 dia",
                    "17 dia", "18 dia", "19 dia", "20 dia", "21 dia"],
                "data": [
                    [197, 191, 176, 166, 150, 149, 128, 125, 118, 108, 98, 85, 77, 66, 57, 49, 34, 26, 16, 6, 0],
                    [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
                ]
            };
            vm.data = vm.respon.data;
            vm.dias = vm.respon.dias;
        }

        //////////////////////////

        $scope.testProyecto = function (id) {
            console.log('El id es: ' + id);
            $http.post('/api/proyect/estado/', {'id': id}).then(
                SuccessFn, ErrorFn
            );
        }
        var SuccessFn = function (data, status, headers, config) {
            console.log('post ejecutado con exito');
            console.log(data);
        }

        var ErrorFn = function (data, status, headers, config) {
            console.error(data.data);
            console.error('Epic failure!');
            console.log(data);
            console.log(status)
        }
    }
})();


