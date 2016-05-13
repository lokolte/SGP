/**
 * Created by Jesus Aguilar on 27/03/2015.
 */
/**
 * Authentication
 * @namespace managers.authentication.services
 */
(function () {
    'use strict';

    angular
        .module('managers.authentication.services')
        .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    /**
     * @namespace Authentication
     * @returns {Factory}
     */
    function Authentication($cookies, $http) {
        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var Authentication = {
            getAuthenticatedUsuario: getAuthenticatedUsuario,
            isAuthenticated: isAuthenticated,
            login: login,
            logout: logout,
            register: register,
            setAuthenticatedUsuario: setAuthenticatedUsuario,
            unauthenticate: unauthenticate
        };

        return Authentication;

        ////////////////////

        /**
         * @name register
         * @desc Try to register a new user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         * @memberOf managers.authentication.services.Authentication
         */
        function register(username, password, email, nombre, apellido) {
            return $http.post('/api/usuarios/', {
                username: username,
                password: password,
                email: email,
                nombre: nombre,
                apellido: apellido
            }).then(registerSuccessFn, registerErrorFn);

            /**
             * @name loginSuccessFn
             * @desc Set the authenticated account and redirect to index
             */
            function registerSuccessFn(data, status, headers, config) {
                //Authentication.login(username, password); //podemos agregar login aca :)
                window.location = '/';
            }

            /**
             * @name loginErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function registerErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        }

        /**
         * @name login
         * @desc Try to log in with email `email` and password `password`
         * @param {string} email The email entered by the user
         * @param {string} password The password entered by the user
         * @returns {Promise}
         * @memberOf managers.authentication.services.Authentication
         */
        function login(username, password) {
            console.log('realiza el post');
            return $http.post('api/login/', {
                username: username, password: password
            }).then(loginSuccessFn, loginErrorFn);

            /**
             * @name loginSuccessFn
             * @desc Set the authenticated account and redirect to index
             */
            function loginSuccessFn(data, status, headers, config) {
                console.log(data.data);
                Authentication.setAuthenticatedUsuario(data.data);

                window.location = '/';
            }

            /**
             * @name loginErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function loginErrorFn(data, status, headers, config) {
                console.error(data.data);
                console.error('Epic failure!');
                console.log(data);
                console.log(status)
            }
        }

        /**
         * @name getAuthenticatedAccount
         * @desc Return the currently authenticated account
         * @returns {object|undefined} Account if authenticated, else `undefined`
         * @memberOf managers.authentication.services.Authentication
         */
        function getAuthenticatedUsuario() {
            if (!Authentication.isAuthenticated()) {
                return;
            }

            return $cookies.getObject('authenticatedUsuario');//JSON.parse($cookies.authenticatedUsuario);
        }

        /**
         * @name isAuthenticated
         * @desc Check if the current user is authenticated
         * @returns {boolean} True is user is authenticated, else false.
         * @memberOf managers.authentication.services.Authentication
         */
        function isAuthenticated() {
            console.log('isAuthenticated: ');
            console.log(!!$cookies.getObject('authenticatedUsuario'));
            return !!$cookies.getObject('authenticatedUsuario');
        }

        /**
         * @name setAuthenticatedAccount
         * @desc Stringify the account object and store it in a cookie
         * @param {Object} usuario The account object to be stored
         * @returns {undefined}
         * @memberOf managers.authentication.services.Authentication
         */
        function setAuthenticatedUsuario(usuario) {
            console.log('Guardando usuario: ');
            console.log(usuario);
            $cookies.putObject('authenticatedUsuario', usuario);//.authenticatedUsuario = JSON.stringify(usuario);
            console.log(Authentication.getAuthenticatedUsuario());
            console.log(Authentication.isAuthenticated());
        }

        /**
         * @name unauthenticate
         * @desc Delete the cookie where the user object is stored
         * @returns {undefined}
         * @memberOf managers.authentication.services.Authentication
         */
        function unauthenticate() {
            //delete
            $cookies.remove('authenticatedUsuario');
        }

        /**
         * @name logout
         * @desc Try to log the user out
         * @returns {Promise}
         * @memberOf thinkster.authentication.services.Authentication
         */
        function logout() {
            return $http.post('/api/logout/')
                .then(logoutSuccessFn, logoutErrorFn);

            /**
             * @name logoutSuccessFn
             * @desc Unauthenticate and redirect to index with page reload
             */
            function logoutSuccessFn(data, status, headers, config) {
                Authentication.unauthenticate();

                window.location = '/';
            }

            /**
             * @name logoutErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function logoutErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        }

    }
})();