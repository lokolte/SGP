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
        }).otherwise('/404');
    }
})();


