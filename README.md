# BRT
- Book seats on your favorite BRT buses in lagos 
 
  [![Build Status](https://travis-ci.com/NonsoAmadi10/BRT.svg?branch=develop)](https://travis-ci.com/NonsoAmadi10/BRT)  [![Coverage Status](https://coveralls.io/repos/github/NonsoAmadi10/BRT/badge.svg?branch=develop)](https://coveralls.io/github/NonsoAmadi10/BRT?branch=develop)
 

## Key Application features
- Log in
-Admin creates bus and trips listings
- View all bookings
- Book a seat
## Technologies Used
DRF (API)
SWAGGER (API Documentation)
PYLINT
### API Documentation
 - 'http://localhost:8000/api/v1/docs/

Development set up
Check that python 3 is installed:
`python --v`
>> Python 3.6.5

Install pipenv:

brew install pipenv (Mac)
pip install pipenv (Windows | Unix)

You might get the error below if you are on a Windows system. Worry not, all you need to do is follow this [instruction](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip) to install pip
>> pip not found

- Clone the flighty repo and cd into it:

>git clone git@github.com:NonsoAmadi10/BRT.git

-Install dependencies:

>pipenv install
- Install dev dependencies to setup development environment:

> pipenv install --dev
- Create a .env file

>SECRET_KEY=<JWT-SECRET-KEY>
>DJANGO_ENV=<YOUR ENVIRONMENT> This should be set to development

- Activate a virtual environment:

 `virtual venv`
- Run the application:

 `python manage.py runserver`
>Django version 2.1.5, using settings 'BRT.settings'
> export PATH=$PATH:/usr/local/sbin
>Deactivate the virtual environment once you're done:
>exit 

#### Run Test

> coverage run --source='.' manage.py test user
### Test coverage

> coverage report
### Generate html report

> coverage html
## Contribution guide
- All proposals for contribution must satisfy the guidelines in the product wiki. When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.This Project shall be utilising a Pivotal Tracker board to track the work done.

### Pull Request Process
- A contributor shall identify a task to be done from the pivotal tracker.If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
The Contributor shall then create a branch off the develop branch where they are expected to undertake the task they have chosen.
