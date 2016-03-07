# AlgoLab

[![Build Status](https://travis-ci.org/Algolab-CMU/Algolab.svg?branch=master)](https://travis-ci.org/Algolab-CMU/Algolab)

## Dependencies
Algolab frontend is built using Django, with external packages [mysqlclient](https://pypi.python.org/pypi/mysqlclient),
[django-friendship](https://github.com/revsys/django-friendship), [djangorestframework](http://www.django-rest-framework.org/) and [django-registration](https://django-registration.readthedocs.org/en/2.0.4/).
Algolab backend is built using [Tango](https://github.com/autolab/Tango) and [Docker](https://www.docker.com/).

## For developers

### News
*Updated Feb-27th*
After you do ```git pull origin develop```, run
```python
pip install django-friendship
python manage.py migrate
```

(If you see something like ```Table already exists```, run
``` python manage.py migrate --fake```,
Or you could just drop the Schema in mySQLworkbench and create a new one named *AlgoLab* again)

Then do ```python manage.py runserver```

I decide not to implement messages between users for now. It is way more complicated than I have expected. And we probably do not need it,
as even Piazza does not support it yet ;)

### Git
Always push the develop branch! Use
```git
git pull origin develop
git push origin develop
```

### Notes
#### Comment
The comment field cannot be accessed in the user_profile for now. Perhaps the only way to fix that is to drop the table...

#### User
Now you cannot register a new user using the registration page as we do not support email activation yet...
If you want to test, you can create user from [commandline](http://stackoverflow.com/questions/18503770/how-to-create-user-from-django-shell) or
from [admin page](http://127.0.0.1:8000/admin) using your local admin account.

Good luck!
