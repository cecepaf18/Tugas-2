import os #.env
# import env3
from flask import Flask, blueprints, jsonify, request
from resources.busMania import busMania_api
import middleware

app4 = Flask(__name__)
app4.register_blueprint(busMania_api, url_prefix = '/api/v1/bus/')
app4.wsgi_app = middleware.SimpleMiddleware(app4.wsgi_app)

# @app4.before_request
#     def satu():
#         print("satu")

@app4.route('/')
def hello_world():
    return "Hello, Cecep"

# @app4.before_request
# def before_request():
#     if request.headers['Authorization'] != "token" :
#         return "Tak Sopan Mau Masuk"

@app4.route('/exp/<name>',methods = ["GET"])
def exp(name):
    if name != 'jhon':
        # abort(404, message = "EOEOEEOEOEOE")
        return jsonify({"message":"Bad Request"}) , 400
    return name

if __name__=='__main__':
    # app4.run(debug=env3.DEBUG, host=env3.HOST, port=env3.PORT)
    app4.run(debug=True, host=os.getenv('HOST'), port=os.getenv('PORT')) #.env

