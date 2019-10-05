#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DJH'

from coroweb import get
import app
from aiohttp import web
import asyncio
from jinja2 import Environment, FileSystemLoader
import orm
from coroweb import add_routes, add_static


@get('/')
async def index(request):
    return b'<h1>Awesome</h1>'


@get('/hello')
async def hello(request):
    return '<h1>hello!</h1>'

if __name__ == '__main__':
    async def init(loop):
        app = web.Application(loop=loop, middlewares=[
                              logger_factory, response_factory])
        init_jinja2(app, filters=dict(datatime=datetime_filter))
        add_routes(app, 'test_view')
        add_static(app)
        srv = await loop.create_server(app.make_handler(), 'localhost', 9000)
        logging.info('server started at http://127.0.0.1:9000...')
        return srv
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
