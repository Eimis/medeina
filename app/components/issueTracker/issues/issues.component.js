'use strict';

var issuesController = function($rootScope, $scope, issuesModel) {

  var ctrl = this;
  ctrl.model = issuesModel;

  ctrl.$onInit = function() {
    console.log('inited CHILD component')
    ctrl.model.listData(ctrl).then(function(resp){
      ctrl.issues = resp.issues;
    });
  };

};

angular
  .module('issueTracker')
  .component('issues', {
    templateUrl: '/static/components/issueTracker/issues/issues.html',
    controller: issuesController,
  });
