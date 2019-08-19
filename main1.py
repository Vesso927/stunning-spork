# -*- coding: utf-8 -*-
# filename: main.py
import web
import traceback
import hashlib

urls = (
    '/wx', 'Handle',
)


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = 'x123x'
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            traceback.print_exc()
            return Argument


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
