
(function () {
  'use strict';

  angular
    .module('managers.sprint', [
      'managers.sprint.controllers',
      'managers.sprint.services'
    ]);

  angular
    .module('managers.sprint.controllers', []);//, ['ui.bootstrap', 'ui.bootstrap.datepicker']);

  angular
    .module('managers.sprint.services', ['ngCookies']);
})();