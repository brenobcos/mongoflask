from http import HTTPStatus
from flask import jsonify
from app.models.dev_model import Dev


def retrieve():
    devs_list = Dev.get_all()
    devs_list = list(devs_list)

    #Alterar o valor da chave _id para string
    for dev in devs_list:
        #dev é um dict
        #dev["_id"] = str(dev["_id"])
        dev.update({"_id": str(dev["_id"])})

        

    return jsonify(devs_list), HTTPStatus.OK