from flask import jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import BackEnd.GlobalInfo.ResponseMessages as mensajitos
import BackEnd.GlobalInfo.Keys as ColabsKey
from bson import ObjectId


if ColabsKey.dbconn==None:
    mongoConnect=MongoClient(ColabsKey.strConnection)
    ColabsKey.dbconn=mongoConnect[ColabsKey.strDBConnection]
    dbUsers=ColabsKey.dbconn["clUsuarios"]
    dbColabs=ColabsKey.dbconn["clColabs"]



def fnGetColabs():
    try:
        arrFinalColab=[]
        objQuery=dbColabs.find({})
        listColab=list(objQuery)
        if len(listColab)!=0:
            for objColab in listColab:
                print(objColab)
                objFormateado={
                    "_id":str(objColab['_id']),
                    "strNomnbre":objColab["strNomnbre"],
                    "strApellido":objColab['strApellido'],
                    "strPuesto":objColab['strPuesto'],
                    "floatSueldo":float(objColab['floatSueldo']),
                    "strRFC":objColab['strRFC'],
                }
                arrFinalColab.append(objFormateado)
        objResponse=mensajitos.succ200.copy()
        objResponse['Respuesta']=arrFinalColab
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fngetColabs",e)
        return jsonify(mensajitos.err500)

def fnGetUsers():
    try:
        arrFinalUser=[]
        objQuery=dbUsers.find({})
        listUser=list(objQuery)
        if len(listUser)!=0:
            for objUser in listUser:
                print(objUser)
                objFormateado={
                    "_id":str(objUser['_id']),
                    "strCorreo":objUser["strCorreo"],
                    "strPassword":objUser['strPassword'],
                    "strRol":objUser['strRol'],
                }
                arrFinalUser.append(objFormateado)
        objResponse=mensajitos.succ200.copy()
        objResponse['Respuesta']=arrFinalUser
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fngetUsers",e)
        return jsonify(mensajitos.err500)

#Modificar Usuario
def fnUpdateUser(id):
    try:

        datos = request.json

        objUpdate = {
            "$set": {
                "strCorreo": datos["strCorreo"],
                "strPassword": datos["strPassword"],
                "strRol": datos["strRol"]
            }
        }

        resultado = dbUsers.update_one(
            {"_id": ObjectId(id)},
            objUpdate
        )

        if resultado.matched_count == 0:
            return jsonify({
                "Mensaje": "Usuario no encontrado"
            }), 404

        return jsonify({
            "Mensaje": "Usuario modificado correctamente"
        })

    except Exception as e:
        print("Error en fnUpdateUser", e)
        return jsonify(mensajitos.err500)


# ELIMINAR UN USUARIO
def fnDeleteUser(id):
    try:

        resultado = dbUsers.delete_one({
            "_id": ObjectId(id)
        })

        if resultado.deleted_count == 0:
            return jsonify({
                "Mensaje": "Usuario no encontrado"
            }), 404

        return jsonify({
            "Mensaje": "Usuario eliminado correctamente"
        })

    except Exception as e:
        print("Error en fnDeleteUser", e)
        return jsonify(mensajitos.err500)


# BUSCAR USUARIO POR URL
def fnFindUser(correo):
    try:

        objQuery = dbUsers.find({
            "strCorreo": correo
        })

        arrFinalUser = []

        for objUser in objQuery:

            objFormateado = {
                "_id": str(objUser["_id"]),
                "strCorreo": objUser["strCorreo"],
                "strPassword": objUser["strPassword"],
                "strRol": objUser["strRol"]
            }

            arrFinalUser.append(objFormateado)

        objResponse = mensajitos.succ200.copy()
        objResponse["Respuesta"] = arrFinalUser

        return jsonify(objResponse)

    except Exception as e:
        print("Error en fnFindUser", e)
        return jsonify(mensajitos.err500)
    

def fnMensajeGet():
    try:
        return jsonify({"Mensaje":"Hola mundo"})
    except Exception as e:
        return jsonify({"Error":str(e)})


    