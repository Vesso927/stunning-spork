# -*- coding: utf-8 -*-

import hashlib
import web


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
            token = "1234"
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print
            "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument


---------------------
版权声明：本文为CSDN博主「Block - Man」的原创文章，遵循CC
4.0
by - sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / qq_34192983 / article / details / 77050932