angular.module('issueTracker')
  .factory('issuesModel', function($http) {

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

    function submitData(issue_pk) {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      var data = {
        solved: true,
      };

      return $http.patch('/issues/' + issue_pk + '/update', data, config)
        .then(function(response) {
          return {'ok': true};
        })
        .catch(function(response) {
          return {'errors': response.data};
        });
    }

    return {
      listData: listData,
      submitData: submitData,
    };
  });
