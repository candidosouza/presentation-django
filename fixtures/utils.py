import random


class Random:

    @staticmethod
    def random_list_lambda(data):
        return lambda x: Random.random_list(data)

    @staticmethod
    def random_list(data):
        count = len(data)
        return data[random.randint(0, count - 1)]

    @staticmethod
    def random_int_lambda(min, max):
        return lambda x: Random.random_int(min, max)

    @staticmethod
    def random_int(min, max):
        return random.randint(min, max)


class Models:
    @staticmethod
    def set_attr_in_models(models, fields, options):
        models_list = models if type(models) is tuple else (models,)
        for model in models_list:
            fields_list = fields if type(fields) is tuple else (fields,)
            for field in fields_list:
                field_inst = model._meta.get_field(field)
                for key, value in options.items():
                    setattr(field_inst, key, value)

    @staticmethod
    def save_models(models):
        for object in models:
            object.save()
