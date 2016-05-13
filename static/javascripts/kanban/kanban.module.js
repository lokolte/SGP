(function () {
  'use strict';

  angular
    .module('managers.kanban', [
      'managers.kanban.controllers',
      'managers.kanban.services'
    ]);

  angular
    .module('managers.kanban.controllers', ['ngCookies']);

  angular
    .module('managers.kanban.services', []);
})();