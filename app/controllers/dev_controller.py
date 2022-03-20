from http import HTTPStatus
from flask import jsonify, request
from app.models.dev_model import Dev


def get_devs():
    devs_list = Dev.get_all()
    devs_list = list(devs_list)

    # Alterar o valor da chave _id para string
    for dev in devs_list:
        # dev é um dict
        # dev["_id"] = str(dev["_id"])
        # dev.update({"_id": str(dev["_id"])})
        Dev.serialize_dev(dev)

    return jsonify(devs_list), HTTPStatus.OK


def create_dev():
    data = request.get_json()
    dev = Dev(**data)
    print(f"{dev.__dict__}")

    dev.create_dev()
    # dev._id = str(dev._id)
    # dev.__dict__["_id"] = str(dev.__dict__["_id"])
    print(f"{dev.__dict__}")

    serialized_dev = Dev.serialize_dev(dev)

    print(f"{dev.__dict__}")

    return serialized_dev.__dict__, HTTPStatus.CREATED


def remove_dev(dev_id: str):
    deleted_dev = Dev.delete_dev(dev_id)

    if not deleted_dev:
        return {"error": f"id {dev_id} not found"}, HTTPStatus.NOT_FOUND
    
    Dev.serialize_dev(deleted_dev)

    return deleted_dev, HTTPStatus.OK

def get_by_gmail():
    devs = Dev.filter_by_gmail()

    serialize_devs = [Dev.serialize_dev(dev) for dev in devs]

    return jsonify(serialize_devs) , HTTPStatus.OK
