import json
import traceback
from datetime import datetime

from flask import request
from typecheck import TypeCheckError

from application.src.common.exceptions.custom_error import InvalidSourceError, CustomError
from application.src.common.response_utils import error_response


def parse_request_for_error(request_obj):
    try:
        request_headers = "Headers: " + json.dumps(dict(request.headers)) + '<br><br>*********'
    except:
        request_headers = ''

    try:
        request_params = "Params: " + json.dumps(request_obj.args.to_dict()) + "<br><br>*********"
    except:
        request_params = ''

    try:
        request_json = "JSON: " + json.dumps(request.get_json(force=True)) + "<br><br>*********"
    except:
        request_json = ''

    request_parsed = '********<br>*******'.join([request_headers, request_params, request_json])

    return request_parsed


class ErrorHandler(object):
    def __init__(self, api_key, app):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.api_key = api_key
        self.app = app

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            try:
                start = datetime.now()
                output = f(*args, **kwargs)
                self.app.logger.info("Time taken for %s is %s", self.api_key,
                                     datetime.now() - start)
                return output
            except KeyError as e:
                exception_trace = traceback.format_exc()
                self.app.logger.error("Exception in %s API:\n%s",
                                      self.api_key, exception_trace)
                self.app.logger.error("Missing key : " + e.message)
                return error_response(400, "{} is required".format(e.message))
            except (ValueError, TypeCheckError) as e:
                exception_trace = traceback.format_exc()
                self.app.logger.error("Exception in %s API:\n%s",
                                      self.api_key, exception_trace)
                return error_response(400, "Bad Request. Incorrect Parameter types")
            except InvalidSourceError as e:
                exception_trace = traceback.format_exc()
                self.app.logger.error("Exception in %s API:\n%s",
                                      self.api_key, exception_trace)
                self.app.logger.error("Invalid Source : " + e.message)
                return error_response(e.error_code, e.msg or "Invalid Source")
            except CustomError as error:
                exception_trace = traceback.format_exc()
                self.app.logger.error("Exception in %s API: %s\n%s",
                                      self.api_key,
                                      error.get_message(),
                                      exception_trace)
                return error_response(error.get_error_code(), error.get_message())
            except:
                exception_trace = traceback.format_exc()
                self.app.logger.error("Exception in %s API:\n%s",
                                      self.api_key, exception_trace)
                return error_response(500, "Internal Server Error")
            finally:
                pass

        return wrapped_f
