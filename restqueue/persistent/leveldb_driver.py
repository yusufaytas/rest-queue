# -*- coding: utf-8 -*-

"""
restqueue.persistent.leveldb_driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Persistent Driver for LevelDB

"""

import plyvel

class LevelDBDriver(object):
    def __init__(self, db_url=None):
        self.db_url = db_url
        if db_url is None:
            self.db_url = "rest.queue.db"
        self.db_handler = plyvel.DB(self.db_url, create_if_missing=True)
    def is_closed(self):
        assert(self.db_handler is not None)
        return self.db_handler.closed
    def close(self):
        self.db_handler.close()
