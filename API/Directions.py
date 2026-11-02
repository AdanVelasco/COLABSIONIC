from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import BackEnd.Functions as Callmethod
import BackEnd.GlobalInfo.ResponseMessages as mensajitos

# Instancia
app = Flask(__name__)
CORS(app)


@app.route('/')
@cross_origin(allow_headers=['content-Type'])
def Getmessage():
    try:
        objResult = Callmethod.fnMensajeGet()
        return objResult
    except Exception as e:
        print("Error en Getmessage", e)
        return jsonify(mensajitos.err500)


@app.route('/getUsers')
@cross_origin(allow_headers=['content-Type'])
def getUsers():
    try:
        objResult = Callmethod.fnGetUsers()
        return objResult
    except Exception as e:
        print("Error en getUsers", e)
        return jsonify(mensajitos.err500)


@app.route('/getColabs')
@cross_origin(allow_headers=['content-Type'])
def getColabs():
    try:
        objResult = Callmethod.fnGetColabs()
        return objResult
    except Exception as e:
        print("Error en getColabs", e)
        return jsonify(mensajitos.err500)


# MODIFICAR USUARIO
@app.route('/updateUser/<id>', methods=['PUT'])
@cross_origin(allow_headers=['content-Type'])
def updateUser(id):
    try:
        objResult = Callmethod.fnUpdateUser(id)
        return objResult
    except Exception as e:
        print("Error en updateUser", e)
        return jsonify(mensajitos.err500)


# ELIMINAR UN USUARIO
@app.route('/deleteUser/<id>', methods=['DELETE'])
@cross_origin(allow_headers=['content-Type'])
def deleteUser(id):
    try:
        objResult = Callmethod.fnDeleteUser(id)
        return objResult
    except Exception as e:
        print("Error en deleteUser", e)
        return jsonify(mensajitos.err500)


# BUSCAR USUARIO POR URL
@app.route('/findUser/<correo>')
@cross_origin(allow_headers=['content-Type'])
def findUser(correo):
    try:
        objResult = Callmethod.fnFindUser(correo)
        return objResult
    except Exception as e:
        print("Error en findUser", e)
        return jsonify(mensajitos.err500)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)