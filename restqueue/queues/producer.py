# -*- coding: utf-8 -*-

"""
restqueue.queues.producer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Producer Base

"""

def create_producer(conn,routing_key=None,on_return=None):
	pass

def send_message(conn,msg,routing_key=None,delivery_mode=None,priority=0):
	pass