# -*- coding: utf-8 -*-

"""
restqueue.queues.consumer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Consumer Class

"""

from kombu import ConsumerMixin, Queue

class QueueConsumer(ConsumerMixin):
	"""QueueConsumer is consumer class definition for Queues that extends the ConsumerMixin"""
	def __init__(self, connection, queue_name, routing_key="", no_ack=False):
		self.connection = connection
		self.queue = Queue(queue_name,routing_key=routing_key)
	def get_consumers(self, Consumer, channel):
		return [Consumer(queues=[self.queue],callback=[self.on_message_received])]
	def on_message_received(self, body, message):
		pass
	def decode_error(self):
		pass
		