from typing import Union
import pymongo
from bson.objectid import ObjectId
import re
from pymongo import ReturnDocument

from app.exceptions.dev_exc import DevIdNotFound

# Database URI/URL
client = pymongo.MongoClient("mongodb://localhost:27017/")
# use turma8
db = client["turma8"]


class Dev:
    def __init__(self, **kwargs):
        #criando o dicionario de forma dinamica para n ficar restrito às chaves name e email
        for key, value in kwargs.items():
            setattr(self, key, value)

        # self.name = kwargs["name"]
        # self.email = kwargs["email"]

    @staticmethod
    def serialize_dev(dev: Union["Dev", dict]):
        if type(dev) is dict:
            dev.update({"_id": str(dev["_id"])})
        elif type(dev) is Dev:
            dev._id = str(dev._id)

        return dev

    @staticmethod
    def get_all():
        devs_list = db.devs.find()

        return devs_list

    def create_dev(self):
        db.devs.insert_one(self.__dict__)

    @staticmethod
    def delete_dev(dev_id: str):
        # db.devs.delete_one() - deleta mais n retorna o elemento deletado
        deleted_dev = db.devs.find_one_and_delete({"_id": ObjectId(dev_id)})
        return deleted_dev

    @staticmethod
    def filter_by_gmail():
        gmail_regex = re.compile("@gmail")

        devs = db.devs.find({"email": gmail_regex})
        return devs

    @staticmethod
    def update_dev(dev_id: str, payload: dict):
        updated_dev_info = db.devs.find_one_and_update(
            {"_id": ObjectId(dev_id)},
            {"$set": payload},
            return_document=ReturnDocument.AFTER,
        )

        if not updated_dev_info:
            raise DevIdNotFound
        return updated_dev_info