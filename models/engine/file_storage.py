#!/usr/bin/python3
"""dsadsd sadsad sad sd"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Object storager and loader"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """retettt  srd fdf sdfds f"""
        return self.__objects

    def new(self, obj):
        """sdsdsd sdsd sad sads a"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """bla blaabalbslbdlksbd s sdsadf """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update([(key, value.to_dict())])
        with open(self.__file_path, "w", encoding='UTF-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """reloads objects and save to dic"""
        try:
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
