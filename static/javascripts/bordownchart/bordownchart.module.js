(function () {
  'use strict';

  angular
    .module('managers.bordownchart', [
      'managers.bordownchart.controllers',
      'managers.bordownchart.services'
    ]);

  angular
    .module('managers.bordownchart.controllers', ['nvd3ChartDirectives','chart.js']);

  angular
    .module('managers.bordownchart.services', []);
})();

