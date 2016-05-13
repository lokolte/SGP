(function () {
  'use strict';

  angular
    .module('managers.bordownchart', [
      'managers.bordownchart.controllers'
    ]);

  angular
    .module('managers.bordownchart.controllers', ['chart.js', 'angularCharts']);
})();