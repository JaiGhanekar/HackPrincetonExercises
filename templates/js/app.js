var app = angular.module('MyoApp', []);

app.controller('MainController', ['$scope', 'myo', function($scope, myo) {
    myo.success(function(data) {
        $scope.athletes = data;
    });
}]);

app.factory('myo', ['$http', function($http) {
    return $http.get("http://127.0.0.1:8000/api/athletes/?format=json")
    .success(function(data) {
        return data;
    })
    .error(function(err) {
        return err;
    });
}]);
