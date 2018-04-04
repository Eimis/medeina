var myApp = angular.module('issueTracker', ['ui.router', 'oc.lazyLoad', ]);

myApp.config(function($stateProvider) {

  //$urlRouterProvider.otherwise('/');

  $stateProvider

  .state('home', {
    url: '/',
    template: '<issue-tracker></issue-tracker>',
    resolve: {
      deps: ['$ocLazyLoad', function($ocLazyLoad) {

        //extra css:
        return $ocLazyLoad.load([
          //'/static/issueTracker/components/issueTracker/issueTracker.css',
        ])
        .then(function(){
          return $ocLazyLoad.load([
            //Main parent component files:
            '/static/issueTracker/components/issueTracker/issueTracker.model.js',
            '/static/issueTracker/components/issueTracker/issueTracker.component.js',

            //Child components:
            '/static/issueTracker/components/issueTracker/issues/issues.model.js',
            '/static/issueTracker/components/issueTracker/issues/issues.component.js',
          ]);
        });

      }]
    }

  });

});
