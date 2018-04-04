'use strict';

var issueTrackerController = function($rootScope, $scope, issueTrackerModel) {

  var ctrl = this;
  ctrl.model = issueTrackerModel;

  ctrl.$onInit = function() {
    console.log('inited')
  };

};

angular
  .module('issueTracker')
  .component('issueTracker', {
    templateUrl: '/static/issueTracker/components/issueTracker/issue-tracker.html',
    controller: issueTrackerController,
  });
