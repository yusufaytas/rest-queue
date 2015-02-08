# -*- coding: utf-8 -*-

"""
restqueue.queues.consumer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Consumer Class

"""

from kombu import Consumer

class QueueConsumer(object):
	"""QueueConsumer is consumer class definition for Queues"""
	def __init__(self, connection):
		self.connection = connection
	def create_consumer(self):
		pass
	def start_consumer(self):
		pass
	def on_message(self):
		pass
	def decode_error(self):
		pass
		