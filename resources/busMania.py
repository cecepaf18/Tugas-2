from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, abort, inputs

busMania = {
    "busMania": [
        {"Nomor":"1", "Bis":"Primajasa", "Jenis Bis":"AC","Tujuan": ["Jakarta", "Cileunyi", "Garut", "Tasik"]},
        {"Nomor":"2", "Bis":"Budiman", "Jenis Bis":"AC","Tujuan": ["Bekasi", "Karawang", "Cileunyi", "Garut"]}  
    ]}

class readAllBusMania(Resource):
    def get(self):
        return busMania

class readOneBusMania(Resource):
    def get(self):
        no = request.args.get('Nomor')
        bis = request.args.get('Bis')
        for data in busMania["busMania"]:
            if data ["Nomor"] == no: 
                return data, 200
            elif data ["Bis"] == bis: 
                return data["Tujuan"], 200

        return abort(400, message="Data tidak ada")

def nomorHaveExist(Nomor):
    for x in busMania["busMania"]:
        if x["Nomor"] == Nomor:
            abort(400, message="Data ada")
    return Nomor

class addBusMania(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "Nomor",
            help = "Nomor tidak ditemukan",
            required = True,
            location = ["json"],
            
        )
        self.reqparse.add_argument(
            "Bis",
            help = "Bis tidak ditemukan",
            required = True,
            location = ["json"],
             
        )
        self.reqparse.add_argument(
            "Jenis Bis",
            help = "Jenis bis tidak ditemukan",
            required = True,
            location = ["json"],
            
        )
        super().__init__
    def post(self):
        args = self.reqparse.parse_args()
        nomorHaveExist(request.json["Nomor"])
        busMania['busMania'].append(request.json)
        return {'message':"Input Data Sucess"},201

class deleteBusMania(Resource):
    def delete(self, Nomor):
        for index in range(len(busMania["busMania"])):
            if busMania["busMania"][index]["Nomor"] == Nomor:
                busMania["busMania"].pop(index)
                return {"message": "Hapus data berhasil"}, 200

class editBusMania(Resource):
    def put(self):
        req = request.json
        args = request.args.get('Nomor')
        for data in busMania ["busMania"]:
            if data["Nomor"] == args:
                data["Bis"] = req["Bis"]
                data["Jenis Bis"] = req["Jenis Bis"]
                data["Tujuan"]=req["Tujuan"]
                
                return {"message": "Edit data berhasil"}, 201
            else:
                return abort(400, message="Data tidak ada")




busMania_api = Blueprint('resources/busMania',__name__)
api = Api(busMania_api)
api.add_resource(readAllBusMania,'readAllBusMania')
api.add_resource(readOneBusMania,'readOneBusMania')
api.add_resource(addBusMania,'addBusMania')
api.add_resource(deleteBusMania,'deleteBusMania/<Nomor>')
api.add_resource(editBusMania,'editBusMania')
