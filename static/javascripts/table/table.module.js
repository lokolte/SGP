(function () {
  'use strict';

  angular
    .module('managers.table', [
      'managers.table.controllers',
      'managers.table.directives'
    ]);

  angular
    .module('managers.table.controllers', ['chart.js', 'angularCharts']); // 'nvd3ChartDirectives',

  angular
    .module('managers.table.directives', []);
})();
