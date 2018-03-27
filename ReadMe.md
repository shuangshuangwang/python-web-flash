# python-web-flash
> Follow this project, we will build a simple python web project using flask framework step by step.

## 进入sqlite

1. windows - 开始 - 所有程序 - Anaconda3 - anaconda prompt
2. f: - cd workspace/github/python-web-flash
3. python

>>> from app import db, models
>>> users = models.User.query.all()
>>> users


## Init sqlite database

1. ./db_create.py
2. ./db_migrate.py

## If need upgrade

1. ./db_upgrade.py
2. ./db_migrate.py

## Run project
./run.py