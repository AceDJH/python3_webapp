#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'DJH'

import time
import uuid
from orm import Model, StringField, BooleanField, FloatField, TextField


def next_id():
  # 最小宽度为15，左边补0
  return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
  __table__ = 'users'
  id = StringField(name=None, primary_key=True,
                   default=next_id, ddl='varchar(50)')
  email = StringField(name=None, primary_key=False,
                      default=None, ddl='varchar(50)')
  passwd = StringField(name=None, primary_key=False,
                       default=None, ddl='varchar(50)')
  admin = BooleanField(name=None, default=False)
  name = StringField(name=None, primary_key=False,
                     default=None, ddl='varchar(50)')
  image = StringField(name=None, primary_key=False,
                      default=None, ddl='varchar(500)')
  # 我认为应为time.time()
  created_at = FloatField(name=None, primary_key=False, default=time.time)


class Blog(Model):
  __table__ = 'blogs'
  id = StringField(name=None, primary_key=True,
                   default=next_id, ddl='varchar(50)')
  user_id = StringField(name=None, primary_key=False,
                        default=None, ddl='varchar(50)')
  user_name = StringField(name=None, primary_key=False,
                          default=None, ddl='varchar(50)')
  user_image = StringField(name=None, primary_key=False,
                           default=None, ddl='varchar(500)')
  name = StringField(name=None, primary_key=False,
                     default=None, ddl='varchar(50)')
  summary = StringField(name=None, primary_key=False,
                        default=None, ddl='varchar(200)')
  content = TextField(name=None, default=None)
  created_at = FloatField(name=None, primary_key=False, default=time.time)


class Comment(Model):
  __table__ = 'comments'
  id = StringField(name=None, primary_key=True,
                   default=next_id, ddl='varchar(50)')
  blog_id = StringField(name=None, primary_key=False,
                        default=None, ddl='varchar(50)')
  user_id = StringField(name=None, primary_key=False,
                        default=None, ddl='varchar(50)')
  user_name = StringField(name=None, primary_key=False,
                          default=None, ddl='varchar(50)')
  user_image = StringField(name=None, primary_key=False,
                           default=None, ddl='varchar(500)')
  content = TextField(name=None, default=None)
  created_at = FloatField(name=None, primary_key=False, default=time.time)
