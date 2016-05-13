(function () {
    'use strict';

    angular
        .module('managers.table.controllers')
        .controller('TableController', TableController);

    TableController.$inject = ['$scope', '$filter', '$http'];

    function TableController($scope, $filter, $http) {
        //var vm = this;
        ///////////////////////////

        $scope.exampleData = [
            {
                "key": "Series 2",
                "values": [[0, 175], [1, 180], [2, 170], [3, 164], [4, 155], [5, 147], [6, 131], [7, 124], [8, 113], [9, 90], [10, 98], [11, 81], [12, 78], [13, 61], [14, 40], [15, 46], [16, 39], [17, 33], [18, 18], [19, 10], [20, 0]]
            }, {
                "key": "Series 1",
                "values": [[0, 200], [1, 190], [2, 180], [3, 170], [4, 160], [5, 150], [6, 140], [7, 130], [8, 120], [9, 110], [10, 100], [11, 90], [12, 80], [13, 70], [14, 60], [15, 50], [16, 40], [17, 30], [18, 20], [19, 10], [20, 0]]
            }
            /*,
             {
             "key": "Series 3",
             "values": [[1025409600000, 0], [1028088000000, -6.3382185140371], [1030766400000, -5.9507873460847], [1033358400000, -11.569146943813], [1036040400000, -5.4767332317425], [1038632400000, 0.50794682203014], [1041310800000, -5.5310285460542], [1043989200000, -5.7838296963382], [1046408400000, -7.3249341615649], [1049086800000, -6.7078630712489], [1051675200000, 0.44227126150934], [1054353600000, 7.2481659343222], [1056945600000, 9.2512381306992], [1059624000000, 11.341210982529], [1062302400000, 14.734820409020], [1064894400000, 12.387148007542], [1067576400000, 18.436471461827], [1070168400000, 19.830742266977], [1072846800000, 22.643205829887], [1075525200000, 26.693972514363], [1078030800000, 29.489903107308], [1080709200000, 30.756096054034], [1083297600000, 27.992822746720], [1085976000000, 29.225852107431], [1088568000000, 30.156836480689], [1091246400000, 24.859678459498], [1093924800000, 24.151326522641], [1096516800000, 26.974088564049], [1099195200000, 30.587369307288], [1101790800000, 35.952410049136], [1104469200000, 42.723169856608], [1107147600000, 40.104326572110], [1109566800000, 42.034940590574], [1112245200000, 41.201940741519], [1114833600000, 35.959307673456], [1117512000000, 40.234785495828], [1120104000000, 43.347252675906], [1122782400000, 49.122142270314], [1125460800000, 46.336213226596], [1128052800000, 45.738022352292], [1130734800000, 40.782535587694], [1133326800000, 46.298919327736], [1136005200000, 46.525174496692], [1138683600000, 49.369518277658], [1141102800000, 51.359233230659], [1143781200000, 54.290790853085], [1146369600000, 56.370809889665], [1149048000000, 52.347251720842], [1151640000000, 52.651049262704], [1154318400000, 49.006082346714], [1156996800000, 53.833722685976], [1159588800000, 57.368751084016], [1162270800000, 62.620657436870], [1164862800000, 67.843814831233], [1167541200000, 70.696236558827], [1170219600000, 75.281054033390], [1172638800000, 75.494257592448], [1175313600000, 80.620943351778], [1177905600000, 87.289875534061], [1180584000000, 93.299043821956], [1183176000000, 91.015859689151], [1185854400000, 88.392797582470], [1188532800000, 94.699212813219], [1191124800000, 103.50183124741], [1193803200000, 111.30811970524], [1196398800000, 101.36138850420], [1199077200000, 98.665003256909], [1201755600000, 87.999132307989], [1204261200000, 85.315653328802], [1206936000000, 82.146119346213], [1209528000000, 90.093146599737], [1212206400000, 99.385987481068], [1214798400000, 84.763092203314], [1217476800000, 82.910191547323], [1220155200000, 90.191781675161], [1222747200000, 66.188819887335], [1225425600000, 47.259186154933], [1228021200000, 40.548648265024], [1230699600000, 42.458784966634], [1233378000000, 41.462207260082], [1235797200000, 35.224936113579], [1238472000000, 40.810117767284], [1241064000000, 55.041351655012], [1243742400000, 59.168485702020], [1246334400000, 60.474654847301], [1249012800000, 67.306616497709], [1251691200000, 70.539019993440], [1254283200000, 77.571962668603], [1256961600000, 72.108784451998], [1259557200000, 80.269048905849], [1262235600000, 84.754250235173], [1264914000000, 83.053938255703], [1267333200000, 88.067497980334], [1270008000000, 97.556993569060], [1272600000000, 96.744762710807], [1275278400000, 87.146301147104], [1277870400000, 76.113331725206], [1280548800000, 84.745960774176], [1283227200000, 80.883421033110], [1285819200000, 98.377963136001], [1288497600000, 104.16094587057], [1291093200000, 101.92699168281], [1293771600000, 109.16314556604], [1296450000000, 115.31506669000], [1298869200000, 126.55944572261], [1301544000000, 118.47392959295], [1304136000000, 121.44619467743], [1306814400000, 120.38970188330], [1309406400000, 114.99946573061], [1312084800000, 110.95959856356], [1314763200000, 86.186386929240], [1317355200000, 62.100425398325], [1320033600000, 78.680507428540], [1322629200000, 73.876351797642], [1325307600000, 70.866962301942], [1327986000000, 80.863709250982], [1330491600000, 86.946444823715]]
             },
             {
             "key": "Series 4",
             "values": [[1025409600000, -7.0674410638835], [1028088000000, -14.663359292964], [1030766400000, -14.104393060540], [1033358400000, -23.114477037218], [1036040400000, -16.774256687841], [1038632400000, -11.902028464000], [1041310800000, -16.883038668422], [1043989200000, -19.104223676831], [1046408400000, -20.420523282736], [1049086800000, -19.660555051587], [1051675200000, -13.106911231646], [1054353600000, -8.2448460302143], [1056945600000, -7.0313058730976], [1059624000000, -5.1485118700389], [1062302400000, -3.0011028761469], [1064894400000, -4.1367265281467], [1067576400000, 1.5425209565025], [1070168400000, 2.7673533607299], [1072846800000, 7.7077114755360], [1075525200000, 9.7565015112434], [1078030800000, 11.396888609473], [1080709200000, 10.013964745578], [1083297600000, 8.0558890950562], [1085976000000, 9.6081966657458], [1088568000000, 11.918590426432], [1091246400000, 7.9945345523982], [1093924800000, 8.3201276776796], [1096516800000, 9.8283954846342], [1099195200000, 11.527125859650], [1101790800000, 16.413657596527], [1104469200000, 20.393798297928], [1107147600000, 17.456308413907], [1109566800000, 20.087778400999], [1112245200000, 17.988336990817], [1114833600000, 15.378490151331], [1117512000000, 19.474322935730], [1120104000000, 20.013851070354], [1122782400000, 24.749943726975], [1125460800000, 23.558710274826], [1128052800000, 24.558915040889], [1130734800000, 22.355860488034], [1133326800000, 27.138026265756], [1136005200000, 27.202220808591], [1138683600000, 31.219437344964], [1141102800000, 31.392355525125], [1143781200000, 33.373099232542], [1146369600000, 35.095277582309], [1149048000000, 30.923356507615], [1151640000000, 31.083717332561], [1154318400000, 31.290690671561], [1156996800000, 34.247769216679], [1159588800000, 37.411073177620], [1162270800000, 42.079177096411], [1164862800000, 44.978191659648], [1167541200000, 46.713271025310], [1170219600000, 49.203892437699], [1172638800000, 46.684723471826], [1175313600000, 48.385458973500], [1177905600000, 54.660197840305], [1180584000000, 60.311838415602], [1183176000000, 57.583282204682], [1185854400000, 52.425398898751], [1188532800000, 54.663538086985], [1191124800000, 60.181844325224], [1193803200000, 62.877219773621], [1196398800000, 55.760611512951], [1199077200000, 54.735280367784], [1201755600000, 45.495912959474], [1204261200000, 40.934919015876], [1206936000000, 40.303777633187], [1209528000000, 47.403740368773], [1212206400000, 49.951960898839], [1214798400000, 37.534590035098], [1217476800000, 36.405758293321], [1220155200000, 38.545373001858], [1222747200000, 26.106358664455], [1225425600000, 4.2658006768744], [1228021200000, -3.5517839867557], [1230699600000, -2.0878920761513], [1233378000000, -10.408879093829], [1235797200000, -19.924242196038], [1238472000000, -12.906491912782], [1241064000000, -3.9774866468346], [1243742400000, 1.0319171601402], [1246334400000, 1.3109350357718], [1249012800000, 9.1668309061935], [1251691200000, 13.121178985954], [1254283200000, 17.578680237511], [1256961600000, 14.971294355085], [1259557200000, 21.551327027338], [1262235600000, 24.592328423819], [1264914000000, 20.158087829555], [1267333200000, 24.135661929185], [1270008000000, 31.815205405903], [1272600000000, 34.389524768466], [1275278400000, 23.785555857522], [1277870400000, 17.082756649072], [1280548800000, 25.248007727100], [1283227200000, 19.415179069165], [1285819200000, 30.413636349327], [1288497600000, 35.357952964550], [1291093200000, 35.886413535859], [1293771600000, 45.003601951959], [1296450000000, 48.274893564020], [1298869200000, 53.562864914648], [1301544000000, 54.108274337412], [1304136000000, 58.618190111927], [1306814400000, 56.806793965598], [1309406400000, 54.135477252994], [1312084800000, 50.735258942442], [1314763200000, 42.208170945813], [1317355200000, 31.617916826724], [1320033600000, 46.492005006737], [1322629200000, 46.203116922145], [1325307600000, 47.541427643137], [1327986000000, 54.518998440993], [1330491600000, 61.099720234693]]
             }*/
        ];

        ////////////////////////////

        $scope.labels = ["1 dia", "2 dia", "3 dia", "4 dia", "5 dia", "6 dia", "7 dia", "8 dia",
            "9 dia", "10 dia", "11 dia", "12 dia", "13 dia", "14 dia", "15 dia", "16 dia",
            "17 dia", "18 dia", "19 dia", "20 dia", "21 dia"];
        $scope.series = ['Series A', 'Series B'];
        $scope.data = [
            [197, 191, 176, 166, 150, 149, 128, 125, 118, 108, 98, 85, 77, 66, 57, 49, 34, 26, 16, 6, 0],
            [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        ];
        $scope.onClick = function (points, evt) {
            console.log(points[0].value, evt);
            console.log('hacer algo!!');
        };

        //////////////////////////

        $scope.proyecto = {};

        $scope.headers = [{"name": "id"}, {"name": "name"}, {"name": "descripcion"}, {"name": "field3"}, {"name": "field4"}, {"name": "field5"}];

        $scope.sort = {
            sortingOrder: 'id',
            reverse: false
        };

        $scope.gap = 5;

        $scope.filteredItems = [];
        $scope.groupedItems = [];
        $scope.itemsPerPage = 5;
        $scope.pagedItems = [];
        $scope.currentPage = 0;
        $scope.items = [
            {
                "id": 1,
                "name": "name 1",
                "description": "description 1",
                "field3": "field3 1",
                "field4": "field4 1",
                "field5 ": "field5 1"
            },
            {
                "id": 2,
                "name": "name 2",
                "description": "description 1",
                "field3": "field3 2",
                "field4": "field4 2",
                "field5 ": "field5 2"
            },
            {
                "id": 3,
                "name": "name 3",
                "description": "description 1",
                "field3": "field3 3",
                "field4": "field4 3",
                "field5 ": "field5 3"
            },
            {
                "id": 4,
                "name": "name 4",
                "description": "description 1",
                "field3": "field3 4",
                "field4": "field4 4",
                "field5 ": "field5 4"
            },
            {
                "id": 5,
                "name": "name 5",
                "description": "description 1",
                "field3": "field3 5",
                "field4": "field4 5",
                "field5 ": "field5 5"
            },
            {
                "id": 6,
                "name": "name 6",
                "description": "description 1",
                "field3": "field3 6",
                "field4": "field4 6",
                "field5 ": "field5 6"
            },
            {
                "id": 7,
                "name": "name 7",
                "description": "description 1",
                "field3": "field3 7",
                "field4": "field4 7",
                "field5 ": "field5 7"
            },
            {
                "id": 8,
                "name": "name 8",
                "description": "description 1",
                "field3": "field3 8",
                "field4": "field4 8",
                "field5 ": "field5 8"
            },
            {
                "id": 9,
                "name": "name 9",
                "description": "description 1",
                "field3": "field3 9",
                "field4": "field4 9",
                "field5 ": "field5 9"
            },
            {
                "id": 10,
                "name": "name 10",
                "description": "description 1",
                "field3": "field3 10",
                "field4": "field4 10",
                "field5 ": "field5 10"
            },
            {
                "id": 11,
                "name": "name 11",
                "description": "description 1",
                "field3": "field3 11",
                "field4": "field4 11",
                "field5 ": "field5 11"
            },
            {
                "id": 12,
                "name": "name 12",
                "description": "description 1",
                "field3": "field3 12",
                "field4": "field4 12",
                "field5 ": "field5 12"
            },
            {
                "id": 13,
                "name": "name 13",
                "description": "description 1",
                "field3": "field3 13",
                "field4": "field4 13",
                "field5 ": "field5 13"
            },
            {
                "id": 14,
                "name": "name 14",
                "description": "description 1",
                "field3": "field3 14",
                "field4": "field4 14",
                "field5 ": "field5 14"
            },
            {
                "id": 15,
                "name": "name 15",
                "description": "description 1",
                "field3": "field3 15",
                "field4": "field4 15",
                "field5 ": "field5 15"
            },
            {
                "id": 16,
                "name": "name 16",
                "description": "description 1",
                "field3": "field3 16",
                "field4": "field4 16",
                "field5 ": "field5 16"
            },
            {
                "id": 17,
                "name": "name 17",
                "description": "description 1",
                "field3": "field3 17",
                "field4": "field4 17",
                "field5 ": "field5 17"
            },
            {
                "id": 18,
                "name": "name 18",
                "description": "description 1",
                "field3": "field3 18",
                "field4": "field4 18",
                "field5 ": "field5 18"
            },
            {
                "id": 19,
                "name": "name 19",
                "description": "description 1",
                "field3": "field3 19",
                "field4": "field4 19",
                "field5 ": "field5 19"
            },
            {
                "id": 20,
                "name": "name 5",
                "description": "description 1",
                "field3": "field3 5",
                "field4": "field4 5",
                "field5 ": "field5 5"
            },
            {
                "id": 21,
                "name": "name 6",
                "description": "description 1",
                "field3": "field3 6",
                "field4": "field4 6",
                "field5 ": "field5 6"
            },
            {
                "id": 22,
                "name": "name 7",
                "description": "description 1",
                "field3": "field3 7",
                "field4": "field4 7",
                "field5 ": "field5 7"
            },
            {
                "id": 23,
                "name": "name 8",
                "description": "description 1",
                "field3": "field3 8",
                "field4": "field4 8",
                "field5 ": "field5 8"
            },
            {
                "id": 24,
                "name": "name 9",
                "description": "description 1",
                "field3": "field3 9",
                "field4": "field4 9",
                "field5 ": "field5 9"
            },
            {
                "id": 25,
                "name": "name 10",
                "description": "description 1",
                "field3": "field3 10",
                "field4": "field4 10",
                "field5 ": "field5 10"
            },
            {
                "id": 26,
                "name": "name 11",
                "description": "description 1",
                "field3": "field3 11",
                "field4": "field4 11",
                "field5 ": "field5 11"
            },
            {
                "id": 27,
                "name": "name 12",
                "description": "description 1",
                "field3": "field3 12",
                "field4": "field4 12",
                "field5 ": "field5 12"
            },
            {
                "id": 28,
                "name": "name 13",
                "description": "description 1",
                "field3": "field3 13",
                "field4": "field4 13",
                "field5 ": "field5 13"
            },
            {
                "id": 29,
                "name": "name 14",
                "description": "description 1",
                "field3": "field3 14",
                "field4": "field4 14",
                "field5 ": "field5 14"
            },
            {
                "id": 30,
                "name": "name 15",
                "description": "description 1",
                "field3": "field3 15",
                "field4": "field4 15",
                "field5 ": "field5 15"
            },
            {
                "id": 31,
                "name": "name 16",
                "description": "description 1",
                "field3": "field3 16",
                "field4": "field4 16",
                "field5 ": "field5 16"
            },
            {
                "id": 32,
                "name": "name 17",
                "description": "description 1",
                "field3": "field3 17",
                "field4": "field4 17",
                "field5 ": "field5 17"
            },
            {
                "id": 33,
                "name": "name 18",
                "description": "description 1",
                "field3": "field3 18",
                "field4": "field4 18",
                "field5 ": "field5 18"
            },
            {
                "id": 34,
                "name": "name 19",
                "description": "description 1",
                "field3": "field3 19",
                "field4": "field4 19",
                "field5 ": "field5 19"
            },
            {
                "id": 35,
                "name": "name 5",
                "description": "description 1",
                "field3": "field3 5",
                "field4": "field4 5",
                "field5 ": "field5 5"
            },
            {
                "id": 36,
                "name": "name 6",
                "description": "description 1",
                "field3": "field3 6",
                "field4": "field4 6",
                "field5 ": "field5 6"
            },
            {
                "id": 37,
                "name": "name 7",
                "description": "description 1",
                "field3": "field3 7",
                "field4": "field4 7",
                "field5 ": "field5 7"
            },
            {
                "id": 38,
                "name": "name 8",
                "description": "description 1",
                "field3": "field3 8",
                "field4": "field4 8",
                "field5 ": "field5 8"
            },
            {
                "id": 39,
                "name": "name 9",
                "description": "description 1",
                "field3": "field3 9",
                "field4": "field4 9",
                "field5 ": "field5 9"
            },
            {
                "id": 40,
                "name": "name 10",
                "description": "description 1",
                "field3": "field3 10",
                "field4": "field4 10",
                "field5 ": "field5 10"
            },
            {
                "id": 41,
                "name": "name 11",
                "description": "description 1",
                "field3": "field3 11",
                "field4": "field4 11",
                "field5 ": "field5 11"
            },
            {
                "id": 42,
                "name": "name 12",
                "description": "description 1",
                "field3": "field3 12",
                "field4": "field4 12",
                "field5 ": "field5 12"
            },
            {
                "id": 43,
                "name": "name 13",
                "description": "description 1",
                "field3": "field3 13",
                "field4": "field4 13",
                "field5 ": "field5 13"
            },
            {
                "id": 44,
                "name": "name 14",
                "description": "description 1",
                "field3": "field3 14",
                "field4": "field4 14",
                "field5 ": "field5 14"
            },
            {
                "id": 45,
                "name": "name 15",
                "description": "description 1",
                "field3": "field3 15",
                "field4": "field4 15",
                "field5 ": "field5 15"
            },
            {
                "id": 46,
                "name": "name 16",
                "description": "description 1",
                "field3": "field3 16",
                "field4": "field4 16",
                "field5 ": "field5 16"
            },
            {
                "id": 47,
                "name": "name 17",
                "description": "description 1",
                "field3": "field3 17",
                "field4": "field4 17",
                "field5 ": "field5 17"
            },
            {
                "id": 48,
                "name": "name 18",
                "description": "description 1",
                "field3": "field3 18",
                "field4": "field4 18",
                "field5 ": "field5 18"
            },
            {
                "id": 49,
                "name": "name 19",
                "description": "description 1",
                "field3": "field3 19",
                "field4": "field4 19",
                "field5 ": "field5 19"
            },
            {
                "id": 50,
                "name": "name 5",
                "description": "description 1",
                "field3": "field3 5",
                "field4": "field4 5",
                "field5 ": "field5 5"
            },
            {
                "id": 51,
                "name": "name 6",
                "description": "description 1",
                "field3": "field3 6",
                "field4": "field4 6",
                "field5 ": "field5 6"
            },
            {
                "id": 52,
                "name": "name 7",
                "description": "description 1",
                "field3": "field3 7",
                "field4": "field4 7",
                "field5 ": "field5 7"
            },
            {
                "id": 53,
                "name": "name 8",
                "description": "description 1",
                "field3": "field3 8",
                "field4": "field4 8",
                "field5 ": "field5 8"
            },
            {
                "id": 54,
                "name": "name 9",
                "description": "description 1",
                "field3": "field3 9",
                "field4": "field4 9",
                "field5 ": "field5 9"
            },
            {
                "id": 55,
                "name": "name 10",
                "description": "description 1",
                "field3": "field3 10",
                "field4": "field4 10",
                "field5 ": "field5 10"
            },
            {
                "id": 56,
                "name": "name 11",
                "description": "description 1",
                "field3": "field3 11",
                "field4": "field4 11",
                "field5 ": "field5 11"
            },
            {
                "id": 57,
                "name": "name 12",
                "description": "description 1",
                "field3": "field3 12",
                "field4": "field4 12",
                "field5 ": "field5 12"
            },
            {
                "id": 58,
                "name": "name 13",
                "description": "description 1",
                "field3": "field3 13",
                "field4": "field4 13",
                "field5 ": "field5 13"
            },
            {
                "id": 59,
                "name": "name 14",
                "description": "description 1",
                "field3": "field3 14",
                "field4": "field4 14",
                "field5 ": "field5 14"
            },
            {
                "id": 60,
                "name": "name 15",
                "description": "description 1",
                "field3": "field3 15",
                "field4": "field4 15",
                "field5 ": "field5 15"
            },
            {
                "id": 61,
                "name": "name 16",
                "description": "description 1",
                "field3": "field3 16",
                "field4": "field4 16",
                "field5 ": "field5 16"
            },
            {
                "id": 62,
                "name": "name 17",
                "description": "description 1",
                "field3": "field3 17",
                "field4": "field4 17",
                "field5 ": "field5 17"
            },
            {
                "id": 63,
                "name": "name 18",
                "description": "description 1",
                "field3": "field3 18",
                "field4": "field4 18",
                "field5 ": "field5 18"
            },
            {
                "id": 64,
                "name": "name 19",
                "description": "description 1",
                "field3": "field3 19",
                "field4": "field4 19",
                "field5 ": "field5 19"
            },
            {
                "id": 65,
                "name": "name 20",
                "description": "description 1",
                "field3": "field3 20",
                "field4": "field4 20",
                "field5 ": "field5 20"
            }
        ];

        var searchMatch = function (haystack, needle) {
            if (!needle) {
                return true;
            }
            return haystack.toLowerCase().indexOf(needle.toLowerCase()) !== -1;
        };

        // init the filtered items
        $scope.search = function () {
            $scope.filteredItems = $filter('filter')($scope.items, function (item) {
                for (var attr in item) {
                    if (searchMatch(item[attr], $scope.query))
                        return true;
                }
                return false;
            });
            // take care of the sorting order
            if ($scope.sort.sortingOrder !== '') {
                $scope.filteredItems = $filter('orderBy')($scope.filteredItems, $scope.sort.sortingOrder, $scope.sort.reverse);
            }
            $scope.currentPage = 0;
            // now group by pages
            $scope.groupToPages();
        };


        // calculate page in place
        $scope.groupToPages = function () {
            $scope.pagedItems = [];

            for (var i = 0; i < $scope.filteredItems.length; i++) {
                if (i % $scope.itemsPerPage === 0) {
                    $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)] = [$scope.filteredItems[i]];
                } else {
                    $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)].push($scope.filteredItems[i]);
                }
            }
        };

        $scope.range = function (size, start, end) {
            var ret = [];
            console.log(size, start, end);

            if (size < end) {
                end = size;
                start = size - $scope.gap;
            }
            for (var i = start; i < end; i++) {
                ret.push(i);
            }
            console.log(ret);
            return ret;
        };

        $scope.prevPage = function () {
            if ($scope.currentPage > 0) {
                $scope.currentPage--;
            }
        };

        $scope.nextPage = function () {
            if ($scope.currentPage < $scope.pagedItems.length - 1) {
                $scope.currentPage++;
            }
        };

        $scope.setPage = function () {
            $scope.currentPage = this.n;
        };

        // functions have been describe process the data for display
        $scope.search();

        //////////////////////////////////

        $scope.testProyecto = function (id) {//fecha anterior 2015-09-25 23:03:05.654997-04
            console.log('El id es: ' + id);
            var uri = '/api/user/' + id + '/proyectos/';
            console.log(uri);///api/proyectos/(?P<pk>[0-9]+)/cambiar_estado/
            $http.post(uri)//, {'estado':'S'})
            //$http.get(uri)
                /*$http.post('/api/proyectos/proyecto', {'id': id, 'nombre': 'Proyecto Ande',
                 'observacion':'Poyecto iniciado con bajos recursos',
                 'fecha_fin': '2015-09-26 23:03:05'})*/
                .then(SuccessFn, ErrorFn);
        };

        function SuccessFn(data, status, headers, config) {
            console.log('post ejecutado con exito');
            console.log(data.data);
            console.log(data);
            //if(status.toString()){}
            console.log(data.status);
        }

        function ErrorFn(data, status, headers, config) {
            console.error(data.data);
            console.error('Epic failure!');
            console.log(data);
            console.log(data.status);
        }

        /////////////////////////////////////////////
        $scope.configulti = {
            title: '', // chart title. If this is false, no title element will be created.
            tooltips: true,
            labels: false, // labels on data points
            // exposed events
            mouseover: function () {
            },
            mouseout: function () {
            },
            click: function () {
            },
            // legend config
            legend: {
                display: true, // can be either 'left' or 'right'.
                position: 'left',
                // you can have html in series name
                htmlEnabled: false
            },
            // override this array if you're not happy with default colors
            colors: [],
            innerRadius: 0, // Only on pie Charts
            lineLegend: 'lineEnd', // Only on line Charts
            lineCurveType: 'cardinal', // change this as per d3 guidelines to avoid smoothline
            isAnimate: true, // run animations while rendering chart
            yAxisTickFormat: 's', //refer tickFormats in d3 to edit this value
            xAxisMaxTicks: 7, // Optional: maximum number of X axis ticks to show if data points exceed this number
            xAxisTickFormat: 's', // refer tickFormats in d3 to edit this value
            waitForHeightAndWidth: false // if true, it will not throw an error when the height or width are not defined (e.g. while creating a modal form), and it will be keep watching for valid height and width values
        };

        $scope.dataulti = {
            series: ['Sales', 'Income', 'Expense', 'Laptops', 'Keyboards'],
            data: [{
                x: "Laptops",
                y: [100, 500, 0],
                tooltip: "this is tooltip"
            }, {
                x: "Desktops",
                y: [300, 100, 100]
            }, {
                x: "Mobiles",
                y: [351]
            }, {
                x: "Tablets",
                y: [54, 0, 879]
            }]
        };
    }
})();

