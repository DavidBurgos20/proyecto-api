from flask import request
from flask_restful import Resource
from ..Components.friend_request_component import FriendRequestComponent
from ..Model.Request.friend_request_request import FriendRequestRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class FriendRequestListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar solicitudes de amistad")
            resultado = FriendRequestComponent.getAllFriendRequests()

            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class FriendRequestCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear solicitud de amistad")
            rq_json = request.get_json()
            new_request = FriendRequestRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = FriendRequestComponent.insertFriendRequest(rq_json['solicitante_id'], rq_json['solicitado_id'])
            if resultado['result']:
                return response_success("Solicitud de amistad creada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class FriendRequestUpdateService(Resource):
    @staticmethod
    def put(request_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de actualizar solicitud de amistad")
            rq_json = request.get_json()
            new_request = FriendRequestRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = FriendRequestComponent.updateFriendRequest(request_id, rq_json['estado'])
            if resultado['result']:
                return response_success("Solicitud de amistad actualizada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class FriendRequestDeleteService(Resource):
    @staticmethod
    def delete(request_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar solicitud de amistad")
            resultado = FriendRequestComponent.deleteFriendRequest(request_id)
            if resultado['result']:
                return response_success("Solicitud de amistad eliminada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
