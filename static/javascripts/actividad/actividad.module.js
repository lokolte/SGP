(function () {
  'use strict';

  angular
    .module('managers.actividad', [
      'managers.actividad.controllers',
      'managers.actividad.services'
    ]);

  angular
    .module('managers.actividad.controllers', []);//, ['ui.bootstrap', 'ui.bootstrap.datepicker']);

  angular
    .module('managers.actividad.services', []);
})();