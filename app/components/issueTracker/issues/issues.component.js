'use strict';

var issuesController = function($rootScope, $scope, issuesModel, $sanitize) {

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
      ctrl.general_errors = null;
      ctrl.field_errors = null;

      if (resp.ok) {
        ctrl.syncIssues();
      } else {
        //we're returning html with some of the general error messages, so this
        //needs to be sanitized first:
        ctrl.general_errors = $sanitize(resp.errors.detail);

        ctrl.field_errors = resp.errors;
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
