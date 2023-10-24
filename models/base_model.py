#!/usr/bin/python3
"""Base Class sdsdd sad"""
import sys
sys.path.append('.')
from uuid import uuid4
from datetime import datetime
import models



class BaseModel:
    """
    A class used to represent an Animal

    """

    def __init__(self, *args, **kwargs):
        """init s sdsdfd dfasdfsfa"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.save()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "id":
                    self.id = value
                if key == "name":
                    self.name = value
                if key == "my_number":
                    self.my_number = value

    def __str__(self):
        """str ssdsdd sdsd jh"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update every time obj is accsesed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dict for seralization"""
        dic = self.__dict__
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
