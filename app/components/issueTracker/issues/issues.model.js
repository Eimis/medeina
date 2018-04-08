angular.module('issueTracker')
  .factory('issuesModel', function($http) {

    //A method to list all current Issues:
    function listData() {

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

    //A method to update Issue status:
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

    //A method for getting statistics related to Issue solving time:
    function getStats() {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      return $http.get('/issues/stats', config)
        .then(function(response) {
          var stats = angular.fromJson(response.data);

          return {
            stats: stats,
          };
        })
        .catch(function(response) {});
    }

    return {
      listData: listData,
      submitData: submitData,
      getStats: getStats,
    };
  });
