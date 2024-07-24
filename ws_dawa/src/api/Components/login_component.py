from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class LoginComponent:

    @staticmethod
    def login(p_email, p_password):
        try:
            result = False
            data = None
            message = None
            sql = "SELECT count(*) as valor FROM Usuarios WHERE correo_electronico = %s AND contraseña = %s"
            record = (p_email, p_password)

            resul_login = DataBaseHandle.getRecords(sql, 1, record)
            if resul_login['result']:
                if resul_login['data']['valor'] > 0:
                    result = True
                    message = 'Login Exitoso'
                else:
                    message = 'Login No Válido'
            else:
                message = resul_login['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

