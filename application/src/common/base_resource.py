from functools import wraps
from flask_restful import Resource


def sanitize_response(response):
    data = None
    status = 200
    headers = {}
    if isinstance(response, tuple) and len(response) is 3:
        (data, status, headers) = response
    if isinstance(response, tuple) and len(response) is 5:
        (status, data, code, message, header) = response
        return status, data, code, message, headers.update(header)
    else:
        data = response
    return data, status, headers


def patch_response_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        response = sanitize_response(resp)
        if isinstance(response, tuple) and len(response) is 5:
            status, data, code, message, headers = response
            data = {"responseData": data,
                    "status": status,
                    "message": message}

            return data, code, headers
        else:
            data, status, headers = response

        if type(data) not in [list, dict]:
            return resp
        patched = isinstance(data, dict) and (
            "errorCode" in data or "responseData" in data
        )

        if not patched:
            data = {
                "responseData": data
            }

        if 'errorCode' in data.keys():
            status = data['errorCode']

        return data, status, headers

    return wrapper


class BaseResource(Resource):
    method_decorators = [
        patch_response_data]
