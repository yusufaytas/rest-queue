# -*- coding: utf-8 -*-

"""
restqueue.persistent.driver.leveldb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Persistent Driver for LevelDB

"""

import plyvel

class LevelDB:
    def __init__(self, db_url=None):
        self.db_url = db_url
        if db_url is None:
            self.db_url = "rest.queue.db"
        self.db_handler = plyvel.DB(self.db_url, create_if_missing=True)
