(function () {
    'use strict';

    angular
        .module('managers.config', ['managers'])
        .config(config);

    config.$inject = ['$locationProvider'];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider) {
        console.log('llamada de config?');
        //$locationProvider.html5Mode(true);
        //$locationProvider.hashPrefix('!');
        $locationProvider.html5Mode(true).hashPrefix('!');
    }
})();