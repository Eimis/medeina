# medeina

A simple issue tracker application

![Preview](https://i.imgur.com/oEUr5xZ.png "Preview")

The setup was tested with:

* pip `9.0.1`
* bower `1.8.4`

Setup:

* Clone this repo
* create a virtual environment `virtualenv virtualenv`
* run `source virtual/bin/activate` to activate your fresh virtual environment
* run `pip install -r requirements.txt` to install backend dependencies
* run `bower install` to install frontend dependencies
* run `cd medeina/ && ./manage.py migrate` to run migrations (sqlite db is used)
* run `./manage.py collectstatic`
* `./manage.py runserver`
* Visit http://localhost:8000/#/ (don't forget the # character!)

Key points:

* When migrations are ran:

   * 5 initial Issue categories are created
   * Initial superuser (credentials: `superuser/superuser`) and staff user is created (credentials: `staff/staff`)
   * 5 initial Issues are created

* Important notes:

   * Issues can be created / modified via Django admin (http://localhost:8000/admin/)
     and the main app interface (marking issues as 'solved', checking statistics, etc.)
     can be done via `http://localhost:8000/#/`
   * The backend is implemented as a RESTful API with `django-rest-framework`,
     permissions, serializers, proper error messages and etc.
   * The backend uses stateful approach, so during state transition some custom
     code can be executed as well (f. ex. an email or notification can be sent,
     see `states.py`)
   * Most of the functionality has docstrings and comments, so the code should
     be self-explanatory
   * The frontend runs as a separate Angular JS (`1.5.0`) single-page-application
     with a component-based architecture, every component has a `*.component.js`,
     `*.model.js` and `*.html` files. See `app/` directory.
   * Currently There's a `<issue-tracker></issue-tracker>` wrapper component
     and inside of it there's a main `<issues></issues>` component which holds
     the core frontend functionality. One can easily move components within
     the app and everything should nicely work autimatically
   * There's 2 main `*css` files which are loaded when a main django view which
     renders the app is instantiated, but later on one can also specify dependant
     css / js files for each component as well and `lazyLoad` them (see: `app/config/config.router.js`)
   * The app is responsive and should work nicely on iPhones as well. Although,
     for the scope of this task, the css is quite messy (because it's a free template
     which was just modified)
   * To run some basic tests, run `./manage.py test`
