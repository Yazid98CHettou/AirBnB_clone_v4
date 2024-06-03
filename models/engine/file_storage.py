#!/usr/bin/python3
"""fileStorage"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for ke, va in self.__objects.items():
                if type(va) == cls:
                    cls_dict[ke] = va
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Add object to storage"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )
    def save(self):
        """Save to file"""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(odict, file)
    def reload(self):
        """reload storage from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for a in json.load(f).values():
                    name = a["__class__"]
                    del a["__class__"]
                    self.new(eval(name)(**a))
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """Delete"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass
    def close(self):
        """reload method."""
        self.reload()

