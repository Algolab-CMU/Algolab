# AlgoLab

[![Build Status](https://travis-ci.org/Algolab-CMU/Algolab.svg?branch=master)](https://travis-ci.org/Algolab-CMU/Algolab)

## Dependencies
Algolab frontend is built using Django, with external packages [mysqlclient](https://pypi.python.org/pypi/mysqlclient), [djangorestframework](http://www.django-rest-framework.org/) and [django-registration](https://django-registration.readthedocs.org/en/2.0.4/).
Algolab backend is built using [Tango](https://github.com/autolab/Tango) and [Docker](https://www.docker.com/).

## For developers

### Git
Always push the develop branch! Use
```git
git pull origin develop
git push origin develop
```

### Notes
Now you cannot register a new user using the registration page as we do not support email activation yet...
If you want to test, you can create user from [commandline](http://stackoverflow.com/questions/18503770/how-to-create-user-from-django-shell) or
from [admin page](http://127.0.0.1:8000/admin) using your local admin account.

Good luck!
