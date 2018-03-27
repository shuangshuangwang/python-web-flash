#!flask/bin/python

import os
import unittest

from app import app,db

from app.models import User

class TestCase(unittest.TestCase):

    def test_make_unique_username(self):
        u = User(username='wangwu', email='ww@qq.com')
        db.session.add(u)
        db.session.commit()
        username = User.make_unique_username('wangwu')
        assert username != 'wangwu'
        u = User(username=username, email='ww2@qq.com')
        db.session.add(u)
        db.session.commit()
        username2 = User.make_unique_username('wangwu')
        assert username2 != 'wangwu'
        assert username2 != username

    