angular.module('issueTracker')
  .factory('issuesModel', function($http) {

    //Synchronizes data with backend server:
    function listData(scope, items) {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      return $http.get('/issues/list', config)
        .then(function(response) {
          var issues = angular.fromJson(response.data);

          return {
            issues: issues,
          };
        })
        .catch(function(response) {});
    }

    return {
      listData: listData,
    };
  });
