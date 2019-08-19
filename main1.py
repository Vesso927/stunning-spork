# -*- coding: utf-8 -*-
# filename: main.py
import web
import traceback
import hashlib

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
