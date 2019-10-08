#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DJH'

' url handlers '

import re
import time
import json
import logging
import hashlib
import base64
import asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    summary = 'lalala'
    blogs = [
        Blog(id='1', name='Blog1', summary=summary,
             created_at=time.time() - 120),
        Blog(id='2', name='Blog2', summary=summary,
             created_at=time.time() - 3600),
        Blog(id='3', name='Blog3', summary=summary,
             created_at=time.time() - 4000)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)
