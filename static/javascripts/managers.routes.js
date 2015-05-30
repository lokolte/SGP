/**
 * Created by Jesus Aguilar on 27/03/2015.
 */
(function () {
    'use strict';

    angular
        .module('managers.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */

    function config($routeProvider) {
        console.log('entro en el click ' + $routeProvider);
        $routeProvider.when('/crearusuario', {
            controller: 'crearUsuarioController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentication/crearUsuario.html'
        }).when('/login', {
            controller: 'LoginController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/login.html'
        }).when('/', {
            controller: 'IndexController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/layout/index.html'
        }).when('/proyectos', {
            controller: 'ProyectosController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/proyecto/proyectos.html'
        }).when('/flujos', {
            controller: 'FlujosController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/flujo/flujos.html'
        }).when('/actividades', {
            controller: 'ActividadesController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/actividad/actividades.html'
        }).when('/sprints', {
            controller: 'SprintsController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/sprint/sprints.html'
        }).when('/userstories', {
            controller: 'UserStoriesController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/userstory/userstories.html'
        }).when('/kanban', {
            controller: 'KanbansController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/kanbans/kanbans.html'
        }).when('/historialus', {
            controller: 'HistorialUSController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/historialuserstories/historialuserstories.html'
        }).when('/historial', {
            controller: 'HistorialController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/historialuserstories/historial.html'
        }).when('/sprintbacklog', {
            controller: 'SprintsBLController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/sprint/sprintbl.html'
        }).when('/productbacklog', {
            controller: 'ProductBLController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/userstory/productbl.html'
        }).otherwise('/404');
    }
})();


