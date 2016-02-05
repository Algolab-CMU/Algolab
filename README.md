# AlgoLab

[![Build Status](https://travis-ci.org/Algolab-CMU/Algolab.svg?branch=master)](https://travis-ci.org/Algolab-CMU/Algolab) (Don't worry about this for now) <br>

## Python2/3
It requires quite a bit work to have python2 and python3 work together if your PC has python2 installed as the default version for python. If you do not know how have python2 and python3 work together, it is OK to use python2 instead.

(I personally use [Pyenv](https://github.com/yyuu/pyenv) to manage different versions of python)

# Installation
* Install mysqlclient using pip
* Install djangorestframework using pip
* Install MySQL (using the tutorial online)
* Add an account to your MySQL database with username='root' and password='root'
* Create a database caused "AlgoLab" in MySQL (in mysql commandline, type CREATE DATABASE AlgoLab)

After this, you should be able to
```
python manage.py runserver
```
then type
```
python manage.py migrate
```
to start working.

## Warning

### Git
* Everyone should create their own branch named "func-user". For example, my branch is called "user-auth-hanqi". And push to that branch only. After you are done, merge the branch back to develop branch. (See: [Git-flow Tutorial](http://nvie.com/posts/a-successful-git-branching-model/)
* For example, when you push, always do
```
git push origin develop
```
or
```
git push origin your_own_branch
```
and never do
```
git push origin master
```
We plan to merge master and develop during every week's meeting only.

* When you pull results, instead of using pull. You should do
```
git fetch origin develop
git merge origin/develop
```
* During the first week, we probably do not need to push feature as we are working our own, but keep in mind we might need it in the future.


### Others
* It is understandable that your code might not compile as it is dependent on others' code. For example, we probably will needs Allison's base.html for every page we use. You can still commit and push under this scenario
* Every issue should be discussed on our Asana Page

Good luck!
