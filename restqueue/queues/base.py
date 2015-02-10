# -*- coding: utf-8 -*-

"""
restqueue.queues.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Base

"""

from kombu import Connection, Producer, Consumer

def parse_url(url):
    """ Parses the url and creates connection object """
    connection = Connection(url)
    return connection
def connect_to_queue(connection,connection_hook=None, connection_hook_params=None):
    connection.connect()
    connection_hook(*connection_hook_params)
def disconnect_from_queue(connection,disconnect_hook=None, disconnect_hook_params=None):
    connection.close()
    disconnect_hook(*disconnect_hook_params)
def get_connection_errors():
    return connection.get_connection_errors