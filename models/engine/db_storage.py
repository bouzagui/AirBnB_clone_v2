#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class  DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None
    def __init__(self):
        """ init """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """

        new_dict = {}
        if cls is not None:
            for row in self.__session.query(cls).all():
                key = "{}.{}".format(row.__class__.__name__, row.id)
                new_dict[key] = row
            return new_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
        return
    
    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()
        return
    
    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)
        return
    
    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        return

    def close(self):
        """ call remove() method on the private session attribute """
        self.__session.remove()
        return