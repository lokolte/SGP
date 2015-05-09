/**
 * Created by Jesus Aguilar on 28/03/2015.
 */
(function () {
  'use strict';

  angular
    .module('managers.authentication', [
      'managers.authentication.controllers',
      'managers.authentication.services'
    ]);

  angular
    .module('managers.authentication.controllers', []);

  angular
    .module('managers.authentication.services', ['ngCookies']);
})();