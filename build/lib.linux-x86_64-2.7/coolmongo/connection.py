#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import Connection
from pymongo.errors import AutoReconnect, DuplicateKeyError

# @package    coolmongo
# @name       PyMongoWrapper
# @author     Umut Aydin - umut.aydin@coolshark.com
# @desc       MongoDB Wrapper with Reconnection Handler
class CoolMongo(object):
    """pymongo.errors.AutoReconnect ve coklu veritabani destekli mongodb baglanti yoneticisi"""
    def __init__(self, host, port, limit):
        self.reconnectLimit = limit
        self.reconnects = 0
        self.hostname = host
        self.port = port

        # main client socket
        self.connection = None
        self.database = None
        self.collection = None

    def connect(self):
        """sunucuya baglanir"""
        try:
            self.connection = Connection(self.hostname, self.port)

        except Exception, error:
            print 'Session Mongo: %s' % error

    def disconnect(self):
        """sunucu baglantisini kapatir"""
        if self.connection:
            try:
                self.connection.disconnect()
            except Exception, error:
                pass

    def switchDatabase(self, database, collection):
        """veritabanlari/koleksiyonlar arasinda gecis yapar"""
        if not self.connection:
            self.connect()

        try:
            self.database = self.connection[database]
            self.collection = self.database[collection]
        except Exception, error:
            pass

        return self

    def insert(self, data):
        """pymongo icerisindeki insert metodu"""
        self.reconnects = 0
        while self.reconnects < self.reconnectLimit:
            try:
                if self.collection:
                    response = self.collection.insert(data)
                    self.reconnects = 0
                    return response
                else:
                    self.reconnects += 1
                    self.connect()

            except AutoReconnect, error:
                print error
                self.reconnects += 1

                self.disconnect()
                self.connect()

            except DuplicateKeyError, error:
                print error
                return False

            except Exception, error:
                print error
                self.reconnects += 1

        return False

    def update(self, record, data, multi=True, upsert=True):
        """pymongo icerisindeki update metodu"""
        self.reconnects = 0
        while self.reconnects < self.reconnectLimit:
            try:
                if self.collection:
                    response = self.collection.update(record, data, multi=multi, upsert=upsert)
                    self.reconnects = 0
                    return response
                else:
                    self.reconnects += 1
                    self.connect()

            except AutoReconnect, error:
                self.reconnects += 1

                self.disconnect()
                self.connect()

            except DuplicateKeyError, error:
                return False

            except Exception, error:
                self.reconnects += 1

        return False

    def find(self, criteria, limit=None, offset=None, sort=None):
        """pymongo icerisindeki find metodu"""
        self.reconnects = 0
        while self.reconnects < self.reconnectLimit:
            try:
                if self.collection:
                    if limit and offset:
                        if sort:
                            response = self.collection.find(criteria).sort(sort.get('field'), sort.get('type')).skip(offset).limit(limit)
                        else:
                            response = self.collection.find(criteria).skip(offset).limit(limit)
                    elif limit:
                        if sort:
                            response = self.collection.find(criteria).sort(sort.get('field'), sort.get('type')).limit(limit)
                        else:
                            response = self.collection.find(criteria).limit(limit)
                    elif offset:
                        if sort:
                            response = self.collection.find(criteria).sort(sort.get('field'), sort.get('type')).skip(offset)
                        else:
                            response = self.collection.find(criteria).skip(offset)
                    else:
                        if sort:
                            response = self.collection.find(criteria).sort(sort.get('field'), sort.get('type'))
                        else:
                            response = self.collection.find(criteria)
                    self.reconnects = 0
                    return response
                else:
                    self.reconnects += 1
                    self.connect()

            except AutoReconnect, error:
                self.reconnects += 1

                self.disconnect()
                self.connect()

            except Exception, error:
                print error
                self.reconnects += 1

        return []

    def find_one(self, criteria):
        """pymongo icerisindeki find_one metodu"""
        self.reconnects = 0
        while self.reconnects < self.reconnectLimit:
            try:
                if self.collection:
                    response = self.collection.find_one(criteria)
                    self.reconnects = 0
                    return response
                else:
                    self.reconnects += 1
                    self.connect()

            except AutoReconnect, error:
                self.reconnects += 1

                self.disconnect()
                self.connect()

            except Exception, error:
                print error
                self.reconnects += 1

        return None

    def remove(self, criteria):
        """pymongo icerisindeki remove metodu"""
        self.reconnects = 0
        while self.reconnects < self.reconnectLimit:
            try:
                if self.collection:
                    response = self.collection.find_one(criteria)
                    self.reconnects = 0
                    return response
                else:
                    self.reconnects += 1
                    self.connect()

            except AutoReconnect, error:
                self.reconnects += 1

                self.disconnect()
                self.connect()

            except Exception, error:
                print error
                self.reconnects += 1

        return None
