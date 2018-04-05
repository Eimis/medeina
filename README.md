# medeina

A simple issue tracker application

The setup was tested with:

* pip `9.0.1`
* bower `1.8.4`

Setup:

* Clone this repo
* create a virtual environment `virtualenv virtualenv`
* run `source virtual/bin/activate` to activate your fresh virtual environment
* run `pip install -r requirements.txt` to install backend dependencies
* run `bower install` to install frontend dependencies
* run `cd medeina/ && ./manage.py migrate` to run migrations
* run `./manage.py collectstatic`
* `./manage.py runserver`
* Visit http://localhost:8000/#/ (don't forget the # character!)

Key points:

* When migrations are ran:

   Initial Issue categories are created
   Initial superuser (credentials: `superuser/superuser`) and staff user is created (credentials: `staff/staff`)
