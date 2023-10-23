#!/usr/bin/python3
"""dsadsd sadsad sad sd"""

import json


class FileStorage:
    """Object storager and loader"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """retettt  srd fdf sdfds f"""
        return self.__objects

    def new(self, obj):
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path) as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """reloads objects and save to dic"""
        try:
            with open(self.__file_path) as file:
                diki = json.load(file)
                for key, value in diki.items():
                    class_name = value['__class__']
                    class_obj = eval(class_name)
                    for key2, val2 in value.items():
                        setattr(class_obj, key2, val2)
                    self.__objects[key] = class_obj
        except Exception:
            pass
