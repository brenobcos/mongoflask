import pymongo

#Database URI/URL
client = pymongo.MongoClient("mongodb://localhost:27017/")
#use turma8
db = client["turma8"]


class Dev:
    @staticmethod
    def get_all():
        devs_list = db.devs.find()

        return devs_list

    def create_dev(self):
        ...

    @staticmethod
    def delete_dev(dev_id: str):
        ...