/**
 * Created by lokolte on 16/05/15.
 */
(function () {
  'use strict';

  angular
    .module('managers.flujo', [
      'managers.flujo.controllers',
      'managers.flujo.services'
    ]);

  angular
    .module('managers.flujo.controllers', []);//, ['ui.bootstrap', 'ui.bootstrap.datepicker']);

  angular
    .module('managers.flujo.services', ['ngCookies']);
})();