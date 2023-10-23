#!/usr/bin/python3
"""Base Class sdsdd sad"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class used to represent an Animal

    """

    def __init__(self):
        """init s sdsdfd dfasdfsfa"""
        self.id = str(uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """str ssdsdd sdsd jh"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update every time obj is accsesed"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dict for seralization"""
        dic = self.__dict__
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
