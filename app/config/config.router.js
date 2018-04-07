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
        //extra js:
        .then(function(){
          return $ocLazyLoad.load([
            '/static/components-font-awesome/css/fontawesome-all.css',
          ]);

        })
        .then(function(){
          return $ocLazyLoad.load([
            //Main parent component files:
            '/static/components/issueTracker/issueTracker.model.js',
            '/static/components/issueTracker/issueTracker.component.js',

            //Child components:
            '/static/components/issueTracker/issues/issues.model.js',
            '/static/components/issueTracker/issues/issues.component.js',
          ]);
        });

      }]
    }

  });

});
