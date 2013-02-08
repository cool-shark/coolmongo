#!/usr/bin/env py/home/umut/Workspace/video-portal-apithon
# -*- coding: utf-8 -*-

from coolmongo.fields import CustomField
from coolmongo.connection import CoolMongo

class CoolMongoModel(object):
    """CoolMongo baglanti yoneticisi ile uyumlu ORM"""
    def build(self, fields, conn, coll):
        """
            Bu metod modelde kullanilacak alanlarin tanimlamalarini yapar.
            fields {'alan_adi': TipClass()} ornegindeki gibi dict olmalidir.
            conn CoolMongo nesnesi olmalidir.
            coll ise string olarak db.collection tanimindaki koleksiyona karsilik gelmektedir.
        """
        self.fields = dict()
        self.connection = None
        self.collection = None
        self.coll_name = None

        if isinstance(conn, CoolMongo):
            self.connection = conn
            self.connection.connect()
        else:
            raise Exception('conn %s yerine CoolMongo nesnesi olmalidir' % type(conn))

        if isinstance(coll, str):
            self.coll_name = coll
        else:
            raise Exception('collection %s yerine str olmalidir' % type(coll))

        if isinstance(fields, dict):
            if len(fields):
                for field in fields:
                    self.fields[field] = fields.get(field)
            else:
                raise Exception('alan bos birakilamaz')
        else:
            raise Exception('bu alan %s yerine DICT olmalidir' % type(fields))

    def set(self, key, value):
        """Bu metod belirtilen alana belirtilen icerigi koyar"""
        if key in self.fields:
            return self.fields.get(key).set(value)
        else:
            self.fields[key] = CustomField(default=value)
            return True

    def get(self, key):
        """Bu metod belirtilen alanin icerigini dondurur"""
        if key in self.fields:
            return self.fields.get(key).get()
        return None

    def switch(self, database, collection=None):
        """Bu veritabanlari arasinda gecis yapar. collection girerseniz modele tanimlanmis olan yerine istediginiz herhangi bir collection a dokumani kaydedebilirsiniz"""
        self.connection.switchDatabase(database, collection if collection else self.coll_name)

    def save(self):
        """Bu metod alanlardaki verileri veritabanina kaydeder. _id alani tanimli ise mevcut olani gunceller, degilse yeni dokuman ekler"""
        if self.get('_id'):
            return self.connection.update({'_id': self.get('_id')}, {'$set': self._export(without_id=True)})
        else:
            return self.connection.insert(self._export())

    def retrieveById(self, doc_id=None):
        """Bu metod belirtilen _id li dokumani model nesnesine yukler. Islem durumunu boolean olarak dondurur"""
        obj = self.find_one({'_id': doc_id if id else self.get('_id')})
        if obj:
            self._import(obj)
            return True
        return False

    def find(self, criteria, limit=None, offset=None, sort=None):
        """pymongo icerisindeki find metodu"""
        return self.connection.find(criteria, limit, offset, sort)

    def find_one(self, criteria):
        """pymongo icerisindeki find_one metodu"""
        return self.connection.find_one(criteria)

    def remove(self, criteria):
        """pymongo icerisindeki remove metodu"""
        return self.connection.remove(criteria)

    def _import(self, data):
        """modeldeki alanlari verilen nesneye gore gunceller"""
        if isinstance(data, dict):
            if len(data):
                for key in data:
                    if data.get(key) is not None:
                        if not self.set(key, data.get(key)):
                            raise Exception('%s %s icin dogru bir veri degil.' % (data.get(key), key))

    def _export(self, filled_only=False, without_id=False):
        """mevcut dokumani dict olarak dondurur"""
        response = dict()
        for field in self.fields:
            if filled_only and not self.fields.get(field).get():
                continue
            if field == '_id' and without_id:
                continue
            response[field] = self.fields.get(field).get()
        return response
