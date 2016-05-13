(function () {
    'use strict';

    angular
        .module('managers.table.directives')
        .directive('customSort', customSort);

    customSort.$inject = ['$scope', '$filter'];

    function customSort($scope, $filter) {

        var directive = {
            restrict: 'A',
            transclude: true,
            scope: {
                order: '=',
                sort: '='
            },
            templateUrl: ' <a ng-click="sort_by(order)">' +
            '    <span ng-transclude></span>' +
            '    <i ng-class="selectedCls(order)"></i>' +
            '</a>',
            link: function (scope) {

                // change sorting order
                scope.sort_by = function (newSortingOrder) {
                    var sort = scope.sort;

                    if (sort.sortingOrder == newSortingOrder) {
                        sort.reverse = !sort.reverse;
                    }

                    sort.sortingOrder = newSortingOrder;
                };


                scope.selectedCls = function (column) {
                    if (column == scope.sort.sortingOrder) {
                        return ('icon-chevron-' + ((scope.sort.reverse) ? 'down' : 'up'));
                    }
                    else {
                        return 'icon-sort'
                    }
                };
            }// end link
        };

        return directive;
    }
})();