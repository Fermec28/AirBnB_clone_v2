#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: path to the JSON file
        __session: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """ create DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        aux = {}
        valid_models = {
            "User": User, "State": State, "City": City,
            "Amenity": Amenity, "Place": Place,
            "Review": Review
        }
        if cls is None:
            for cls_aux in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(cls_aux).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    aux[key] = obj
        elif type(cls) is str and cls in valid_models:
            for obj in self.__session.query(valid_models[cls]).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                aux[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                aux[key] = obj
        return aux

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """ create session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def delete(self, obj=None):
        """delete object from __objects """

        if obj:
            obj.delete(synchronize_session=False)
            self.__session.commit()

    def find(self, cls, id):
        """find specific object from db """
        return self.__session.query(cls).get(id)

    def close(self):
        """ close session"""
        self.__session.close()
