#!/usr/bin/env py/home/umut/Workspace/video-portal-apithon
# -*- coding: utf-8 -*-

from datetime import datetime, date
from re import match
from bson.objectid import ObjectId
from bson.dbref import DBRef

class StringField(object):
    """String tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default, min_length, max_length, regex"""
    def __init__(self, **kwargs):
        # min_length, max_length, regex
        self.validations= dict()
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and (isinstance(kwargs.get(key), str) or isinstance(kwargs.get(key), unicode)):
                    self.value = kwargs.get(key)

                else:
                    self.validations[key] = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, str) and not isinstance(data, unicode):
            status = False

        if status and len(self.validations):
            for validation in self.validations:
                if status and validation == 'min_length':
                    if len(data) < self.validations.get(validation):
                        status = False

                elif status and validation == 'max_length':
                    if len(data) > self.validations.get(validation):
                        status = False

                elif status and validation == 'regex':
                    if not match(self.validations.get(validation), data):
                        status = False

        return status

class BooleanField(object):
    """Boolean tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default"""
    def __init__(self, **kwargs):
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), bool):
                    self.value = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, bool):
            status = False

        return status

class IntField(object):
    """Integer tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default, min_value, max_value"""
    def __init__(self, **kwargs):
        # min_value, max_value
        self.validations= dict()
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and (isinstance(kwargs.get(key), int) or isinstance(kwargs.get(key), long)):
                    self.value = kwargs.get(key)

                else:
                    self.validations[key] = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, int) and not isinstance(data, long):
            status = False

        if status and len(self.validations):
            for validation in self.validations:
                if status and validation == 'min_value':
                    if data < self.validations.get(validation):
                        status = False

                elif status and validation == 'max_value':
                    if data > self.validations.get(validation):
                        status = False

        return status

class FloatField(object):
    """Float tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default, min_value, max_value"""
    def __init__(self, **kwargs):
        # min_value, max_value
        self.validations= dict()
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), float):
                    self.value = kwargs.get(key)

                else:
                    self.validations[key] = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data
        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, float):
            status = False

        if status and len(self.validations):
            for validation in self.validations:
                if status and validation == 'min_value':
                    if data < self.validations.get(validation):
                        status = False

                elif status and validation == 'max_value':
                    if data > self.validations.get(validation):
                        status = False

        return status

class ListField(object):
    """List tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default, limit"""
    def __init__(self, **kwargs):
        self.validations= dict()
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), list):
                    self.value = kwargs.get(key)
                else:
                    self.validations[key] = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, list):
            status = False

        if status and len(self.validations):
            for validation in self.validations:
                if status and validation == 'limit':
                    if len(data) > self.validations.get(validation):
                        status = False

        return status

class DictField(object):
    """Dictionary tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default, limit"""
    def __init__(self, **kwargs):
        self.value = None
        self.validations= dict()

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), dict):
                    self.value = kwargs.get(key)
                else:
                    self.validations[key] = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, dict):
            status = False

        if status and len(self.validations):
            for validation in self.validations:
                if status and validation == 'limit':
                    if len(data) > self.validations.get(validation):
                        status = False

        return status

class ObjectField(object):
    """bson.objectid.ObjectId tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default"""
    def __init__(self, **kwargs):
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), ObjectId):
                    self.value = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, ObjectId):
            status = False

        return status

class DateTimeField(object):
    """datetime.datetime tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default"""
    def __init__(self, **kwargs):
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), datetime):
                    self.value = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, datetime):
            status = False

        return status

class DateField(object):
    """datetime.date tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default"""
    def __init__(self, **kwargs):
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default' and isinstance(kwargs.get(key), date):
                    self.value = kwargs.get(key)

    def set(self, data):
        validation = self.validate(data)
        if validation:
            self.value = data

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if not isinstance(data, date):
            status = False

        return status

class ReferenceField(object):
    """bson.objectid.ObjectId tipi icin MongoDB alan yoneticisi. Alabildigi parametreler: default"""
    def __init__(self, **kwargs):
        self.value = None
        self.collection = None

        if len(kwargs):
            if kwargs.has_key('collection') and (isinstance(kwargs.get('collection'), str) or isinstance(kwargs.get('collection'), unicode)):
                self.collection = kwargs.get('collection')
            else:
                raise Exception('unknown collection for reference field')

            for key in kwargs:
                if key != 'collection':
                    if key == 'default' and isinstance(kwargs.get(key), ObjectId):
                        self.value = DBRef(self.collection, kwargs.get(key))

    def set(self, data):
        if not data:
            self.value = None
            return True

        validation = self.validate(data)
        if validation:
            if isinstance(data, DBRef):
                self.value = DBRef(data.collection, data.id)
            else:
                self.value = DBRef(self.collection, data)

        return validation

    def get(self):
        return self.value

    def validate(self, data):
        status = True
        if isinstance(data, DBRef):
            status = True
        elif not isinstance(data, ObjectId):
            status = False

        return status

class CustomField(object):
    """Veri tipinden bagimsiz MongoDB alan yoneticisi. Alabildigi parametreler: default"""
    def __init__(self, **kwargs):
        self.value = None

        if len(kwargs):
            for key in kwargs:
                if key == 'default':
                    self.value = kwargs.get(key)

    def set(self, data):
        self.value = data

    def get(self):
        return self.value


