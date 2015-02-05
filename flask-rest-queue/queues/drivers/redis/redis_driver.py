# -*- coding: utf-8 -*-

"""
restqueue.queue.driver.redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue Driver for Redis

"""

import redis

class RedisDriver:
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        self.redis_pool = redis.ConnectionPool(host=host,port=port,db=db,password=password)
    def create_connection(self):
        assert(self.redis_pool is not None)
        self.redis_conn = redis.StrictRedis(connection_pool=self.redis_pool)
    def end_pool_connection(self):
        assert(self.redis_pool is not None)
        self.redis_pool.disconnect()
    def create_pubsub(self):
        assert(self.redis_conn is not None)
        return self.redis_conn.pubsub()
    def subscriber_listener(self,pubsub,queue_name,callback_func=None,callback_attr=None):
        assert(pubsub is not None)
        pubsub.subscribe(queue_name)
        for message in pubsub.listen():
            if message['type'] == 'message':
                #Call Callback Function
                print "New Message: %s" % (message)
                if callback_func is not None and callback_attr is not None:
                    callback_func(*callback_attr)
    def publish(self,queue_name,message,callback_func=None,callback_attr=None):
        assert(self.redis_conn is not None)
        self.redis_conn.publish(queue_name,message)
        print "Message Sent: %s" %(message)
        if callback_func is not None and callback_attr is not None:
            callback_func(*callback_attr)
