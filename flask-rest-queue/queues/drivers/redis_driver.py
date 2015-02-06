# -*- coding: utf-8 -*-

"""
restqueue.queue.driver.redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Driver for Redis

"""

import redis

class RedisDriver:
    def __init__(self, persistent=False,host='localhost', port=6379, db=0, password=None):
        self.redis_pool = redis.ConnectionPool(host=host,port=port,db=db,password=password)
        self.persistent = persistent
    def create_connection(self):
        """Creates a new connection from Connection Pool"""
        assert self.redis_pool is not None
        self.redis_conn = redis.StrictRedis(connection_pool=self.redis_pool)
    def end_pool_connection(self):
        """Closes the Pool Connection"""
        assert self.redis_pool is not None
        self.redis_pool.disconnect()
    def create_pubsub(self):
        """Creates PubSub Handler"""
        assert self.redis_conn is not None
        self.pubsub = self.redis_conn.pubsub()
    def subscriber_listener(self,queue_name,callback_func=None):
        """Listener for the Subscriber"""
        assert queue_name is not None

        if self.persistent is False:
            assert self.pubsub is not None
            self.pubsub.subscribe(queue_name)
            for message in pubsub.listen():
                if message['type'] == 'message':
                    #Call Callback Function
                    print "New Message: %s" % (message)
                    if callback_func is not None:
                        callback_func(message['data'])
        else:
            while True:
                message = self.redis_conn.blpop(queue_name)
                #Call Callback Function
                print "New Message: %s" % (message)
                if callback_func is not None:
                    callback_func(message[1])
                
    def publish(self,queue_name,message,callback_func=None,callback_attr=None):
        """Publishes new message to the Queue"""
        assert self.redis_conn is not None
        if self.persistent is False:
            self.redis_conn.publish(queue_name,message)
            print "Message Sent: %s" %(message)
        else:
            self.redis_conn.rpush(queue_name,message)

        if callback_func is not None and callback_attr is not None:
            callback_func(*callback_attr)
