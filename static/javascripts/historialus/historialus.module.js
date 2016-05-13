(function () {
  'use strict';

  angular
    .module('managers.historialus', [
      'managers.historialus.controllers',
      'managers.historialus.services'
    ]);

  angular
    .module('managers.historialus.controllers', []);

  angular
    .module('managers.historialus.services', ['ngCookies']);
})();