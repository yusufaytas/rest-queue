# -*- coding: utf-8 -*-

"""
restqueue.queues.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Base Class

"""

import os

try:
    import urlparse
except:
    import urllib.parse as urlparse

DRIVERS = {
        'redis' : 'restqueue.queues.drivers.redis_driver',
        'rabbitmq' : 'restqueue.queues.drivers.rabbitmq_driver',
        'mongodb' : 'restqueue.queues.drivers.mongodb_driver',
        'qpid' : 'restqueue.queues.drivers.qpid_driver',
        'sqs' : 'restqueue.queues.drivers.sqs_driver',
        'zaqar' : 'restqueue.queues.drivers.zaqar_driver',
        'nsq' : 'restqueue.queues.drivers.nsq_driver',
        'memcached' : 'restqueue.queues.drivers.memcached_driver'
}

class QueueBase:
    def __init__(self, url):
        self.url = url
    def parse_url(self):
        """ This method's main idea is taken from the Kenneth Reitz's dj-database-url """

        #TODO: Other Message Queues should be added here
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
    def get_queue_driver(self):
        self.parse_url()
        return DRIVERS[self.parsed_url['engine']]
