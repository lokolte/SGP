
(function () {
    'use strict';

    angular
        .module('managers.proyecto.controllers')//, ['ui.bootstrap', 'ui.bootstrap.datepicker'])
        .controller('ProyectosController', ProyectosController);

    ProyectosController.$inject = ['$location', '$scope', '$filter', 'Proyectos', 'Authentication'];

    function ProyectosController($location, $scope, $filter, Proyectos, Authentication) {

        var vm = this;
        vm.proyectos = [];
        vm.proyecto = {};

        vm.clientes = [];

        vm.eNulo = {};
        vm.ownerNulo = {};
        vm.proyectoNulo = {};
        vm.cNulo = {};

        vm.idEstado = {};
        vm.idEstado.e = {};


        vm.idCliente = {};
        vm.idCliente.c = {};


        vm.cambiarEstado = cambiarEstado;
        vm.editar = editar;
        vm.guardar = guardar;
        vm.clear = clear;

        vm.irFlujos = irFlujos;
        vm.definirEstadoCliente = definirEstadoCliente;
        vm.agregarEstado = agregarEstado;
        vm.irSprint = irSprint;
        vm.agregarCliente = agregarCliente;
        vm.ponerFechas = ponerFechas;
        vm.irBordownchart = irBordownchart;

        activate();

        init();

        function inicializar(){

            vm.ownerNulo = {
                "id": 0,
                "email": '',
                "username": '',
                "fecha_creacion": new Date(),
                "fecha_modificacion": new Date(),
                "nombre": '',
                "apellido": '',
                "telefono": '',
                "direccion": ''
            };

            vm.proyectoNulo = {
                "id": 0,
                "nombre": '',
                "owner": vm.ownerNulo,
                "fecha_creacion": new Date(),
                "estado": '',
                "fecha_ini": new Date(),
                "fecha_fin": new Date(),
                "observacion": ''
            };

            vm.clientes = [{
                "id": 3,
                "email": "anastacia@gmail.com",
                "username": "anastacia",
                "fecha_creacion": "2015-06-18T19:21:23.085536Z",
                "fecha_modificacion": "2015-06-18T19:21:23.096716Z",
                "nombre": "Anastacia",
                "apellido": "Bogado",
                "telefono": "123",
                "direccion": "colo323"
            }];

            vm.eNulo = {
                'id': 0,
                'estado': '',
                'key': ''
            };

            vm.estados = [
                {
                    'id': 1,
                    'estado': 'Activo',
                    'key': 'A'
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

            vm.cNulo = {
                "id": 0,
                "email": '',
                "username": '',
                "fecha_creacion": new Date(),
                "fecha_modificacion": new Date(),
                "nombre": '',
                "apellido": '',
                "telefono": '',
                "direccion": ''
            };

            vm.idEstado.e = vm.eNulo;
            vm.idCliente.c = vm.cNulo;
            vm.proyecto = vm.proyectoNulo;
        }

        function init() {

            inicializar();
            clear();

            vm.proyecto = vm.proyectoNulo;

            console.log('ejecutado el post?? primero??');

            extraerProyectos();

            console.log('ejecutado el post??');

            console.log(vm.proyectos)

        }

        function activate() {

            if (!Authentication.isAuthenticated()) {
                $location.url('/login');
            }

        }

        function ponerFechas() {
            var i = 0;
            console.log('Llega?..');
            for (i = 0; i < vm.proyectos.length; i++) {
                console.log('Iteracion: ' + i);
                vm.proyectos[i].fecha_creacion = new Date(Date.parse(vm.proyectos[i].fecha_creacion));
                console.log('Iteracion: ' + i);
                vm.proyectos[i].fecha_ini = new Date(Date.parse(vm.proyectos[i].fecha_ini));
                console.log('Iteracion: ' + i);
                vm.proyectos[i].fecha_fin = new Date(Date.parse(vm.proyectos[i].fecha_fin));
                console.log('Iteracion: ' + i);
                vm.proyectos[i].owner.fecha_creacion = new Date(Date.parse(vm.proyectos[i].owner.fecha_creacion));
                vm.proyectos[i].owner.fecha_modificacion = new Date(Date.parse(vm.proyectos[i].owner.fecha_modificacion));
            }
        }

        function guardar() {

            var i = 0;
            var found = {};
            for (i = 0; i < vm.proyectos.length; i++) {
                if (vm.proyecto.id == vm.proyectos[i].id) {
                    found = vm.proyectos[i];
                    break;
                }
            }

            console.log(!found);
            console.log(found);

            if (!!(found)) {
                console.log('intentando crear y desplegar de nuevo los proyectos...');
                console.log(vm.proyecto);
                console.log('creando....');
                crearProyecto(vm.proyecto);
                extraerProyectos();

                console.log(vm.proyecto);
                console.log(vm.proyectos);
            }
            clear();
        }

        function cambiarEstado(/**/) {
            //Proyectos.cambiarEstado(/*datos del Estado*/);
        }

        function editar(proyecto_input) {
            vm.proyecto = proyecto_input;
            console.log(vm.proyecto);
            //definirEstadoCliente(vm.proyecto.estado, vm.proyecto);
            console.log('EL estado es: ' + vm.proyecto.estado);
            //console.log('El cliente es: ' + vm.proyecto.cliente.nombre);
            //vm.idCliente.c = vm.proyecto.cliente;
            //console.log('Cliente agregado: ' + vm.idCliente.c.nombre);
        }

        function clear() {
            vm.idEstado.e = vm.eNulo;
            //vm.idCliente.c = vm.cNulo;
            vm.proyecto = vm.proyectoNulo;
        }

        function irFlujos(proyecto) {
            Proyectos.setProyectoCookie(proyecto);
            $location.url('/flujos');
        }

        function definirEstadoCliente(e, c) {
            if (e == 'Activo' || e == 'A') {
                vm.idEstado.e = vm.estados[0];
            } else if (e == 'Suspendido' || e == 'S') {
                vm.idEstado.e = vm.estados[1];
            } else if (e == 'Finalizado' || e == 'F') {
                vm.idEstado.e = vm.estados[2];
            }
            //vm.idCliente.c = buscarCliente(c);
            console.log(vm.idEstado.e);
            console.log('El cliente es: ');
            console.log(vm.idCliente.c);
            console.log('exito cliente?');
        }

        function buscarCliente(c) {
            var i = 0;
            var found = {};
            for (i = 0; i < vm.clientes.length; i++) {
                if (c.id == vm.clientes[i].id) {
                    found = vm.clientes[i];
                    return found;
                }
            }
        }

        function agregarEstado() {
            if (!!vm.idEstado.e) {
                var estado = vm.idEstado.e;
                console.log('entro hasta aqui en estados');
                console.log(estado);
                vm.proyecto.estado = vm.estados[estado.id - 1].key;
                console.log(vm.proyecto.estado);
            }
        }

        function irSprint(proyecto) {
            Proyectos.setProyectoCookie(proyecto);
            $location.url('/sprints');
        }

        function irBordownchart(proyecto) {
            Proyectos.setProyectoCookie(proyecto);
            $location.url('/bordownchart');
        }

        function agregarCliente() {
            if (!!vm.idCliente.c) {
                var cliente = vm.idCliente.c;
                console.log('entro hasta aqui en clientes');
                console.log(cliente);
                vm.proyecto.estado = cliente;
                console.log(vm.proyecto.cliente);
            }
        }

        function crearProyecto(proyecto) {

            console.log('intentando crear el elemento con datos: ');
            console.log(proyecto);

            proyecto.owner = Authentication.getAuthenticatedUsuario();
            proyecto.fecha_creacion = new Date();

            Proyectos.create(proyecto).then(SuccessFn, ErrorFn);

            function SuccessFn(data, status, headers, config) {
                console.log('post ejecutado con exito');
                console.log(data.data);
                //vm.proyecto = data.data;
                console.log(data);
                console.log(data.status);
            }

            function ErrorFn(data, status, headers, config) {
                console.error(data.data);
                console.error('Epic failure!');
                console.log(data);
                console.log(data.status);
            }
        }

        function extraerProyectos() {

            Proyectos.all().then(SuccessFn, ErrorFn);

            function SuccessFn(data, status, headers, config) {
                console.log('post ejecutado con exito');
                console.log(data.data);
                vm.proyectos = data.data;
                ponerFechas();
                console.log(data);
                console.log(data.status);
            }

            function ErrorFn(data, status, headers, config) {
                console.error(data.data);
                console.error('Epic failure!');
                console.log(data);
                console.log(data.status);
            }
        }
    }
})();