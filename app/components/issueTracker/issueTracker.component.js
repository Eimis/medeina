'use strict';

var issueTrackerController = function($rootScope, $scope, issueTrackerModel) {

  var ctrl = this;
  ctrl.model = issueTrackerModel;

  ctrl.$onInit = function() {
  };

};

angular
  .module('issueTracker')
  .component('issueTracker', {
    templateUrl: '/static/components/issueTracker/issue-tracker.html',
    controller: issueTrackerController,
  });
