# -*- coding: utf-8 -*-

"""
restqueue.queue.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Base Class

"""

import os

try:
    import urlparse
except:
    import urllib.parse as urlparse

class QueueBase:
    def __init__(self, url):
        self.url = url
    def parse_url(self):
        """ This method's main idea is taken from the Kenneth Reitz's dj-database-url """
        urlparse.uses_netloc.append('redis')
        urlparse.uses_netloc.append('rabbitmq')
        urlparse.uses_netloc.append('mongodb')

        url = urlparse.urlparse(self.url)

        path = url.path[1:]
        path = path.split('?', 2)[0]

        engine = url.schema
        hostname = url.hostname
        user = url.username
        password = url.password
        port = url.port

        self.parsed_url = {'engine':engine, 'hostname':hostname, 'username': user,
                            'password': password, 'port': port}

