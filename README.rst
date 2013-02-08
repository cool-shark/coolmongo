About
========

Simple MongoDB ORM with Live Database Switch Feature


Usage
========

    from coolmongo.fields import *
    from coolmongo.orm import CoolMongoModel
    from coolmongo.connection import CoolMongo

    mongo_connection = CoolMongo('127.0.0.1', 27017, 5)

    class TestModel(CoolMongoModel):
        def __init__(self, data=None):
            self.build({
               'field1' : StringField(min_length=1, max_length=200),
               'field2' : BooleanField(default=False),
            }, mongo_connection, 'database_name')
            self._import(data)

    test_instance = TestModel({
        'field1': 'Test',
        'field2': False
    })
    test_instance.save()

    print test_instance._export(without_id=True)

    test_instance.set('field2', True)
    test_instance.save()

    print test_instance._export(without_id=True)
