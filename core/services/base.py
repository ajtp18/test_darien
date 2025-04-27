from typing import TypeVar, Generic, Type
from django.db import models

T = TypeVar('T', bound=models.Model)

class BaseService(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    def get_all(self):
        return self.model_class.objects.all()

    def get_by_id(self, id):
        return self.model_class.objects.get(pk=id)

    def create(self, **kwargs):
        return self.model_class.objects.create(**kwargs)

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete() 