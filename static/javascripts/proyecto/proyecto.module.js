/**
 * Created by lokolte on 09/05/15.
 */
(function () {
  'use strict';

  angular
    .module('managers.proyecto', [
      'managers.proyecto.controllers',
      'managers.proyecto.services'
    ]);

  angular
    .module('managers.proyecto.controllers', []);//, ['ui.bootstrap', 'ui.bootstrap.datepicker']);

  angular
    .module('managers.proyecto.services', []);
})();