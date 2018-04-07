'use strict';

var issuesController = function($rootScope, $scope, issuesModel) {

  var ctrl = this;
  ctrl.model = issuesModel;

  ctrl.$onInit = function() {
    ctrl.syncIssues();
  };

  ctrl.syncIssues = function() {
    ctrl.model.listData(ctrl).then(function(resp){
      ctrl.issues = resp.issues;
    });
  };

  ctrl.markAsSolved = function(issue_pk) {

    ctrl.model.submitData(issue_pk).then(function(resp){
      if (resp.ok) {
        ctrl.syncIssues();
      } else {
        ctrl.errors = resp.errors;
      }
    });

  };

};

angular
  .module('issueTracker')
  .component('issues', {
    templateUrl: '/static/components/issueTracker/issues/issues.html',
    controller: issuesController,
  });
