# -*- coding: utf-8 -*-

"""
restqueue.queues.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Base Class

"""

from kombu import Connection, Producer, Consumer

class QueueBase:
    def __init__(self, url, timeout=None, transport_options=None, is_pool_enabled=False):
        self.url = url
        self.timeout = timeout
        self.transport_options = transport_options
        self.is_pool_enabled = is_pool_enabled
    def parse_url(self):
        """ Parses the url and creates connection object """
        self.connection = Connection(self.url)
    def get_queue_driver(self):
        self.parse_url()
        return DRIVERS[self.parsed_url['engine']]
    def connect(self, connection_hook=None, connection_hook_params=None):
        self.connection.connect()
        connection_hook(*connection_hook_params)
    def disconnect(self, disconnect_hook=None, disconnect_hook_params=None):
        self.connection.close()
        disconnect_hook(*disconnect_hook_params)
    def create_producer(self):
        pass
    def publish_message(self):
        pass
    def create_consumer(self):
        pass