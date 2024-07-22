import logging
import inspect
from logging import Logger
from pydantic import BaseModel
from logging.handlers import TimedRotatingFileHandler


# file_handler = logging.FileHandler("app.log")
file_handler = TimedRotatingFileHandler("./logs/app.log", interval=1, when="d")
formatter = logging.Formatter("%(asctime)s - %(caller_path)-35s:%(caller_lineno)-5d - %(levelname)-8s - %(message)s")
file_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

def __toLog(logger: Logger, resp:BaseModel | dict, atype:int):
    caller_filename = inspect.stack()[2].filename
    caller_lineno = inspect.stack()[2].lineno
    other_params = None
    match atype:
        case 0:
            _log = logger.info
        case 1:
            _log = logger.debug
        case 2:
            _log = logger.error
            other_params = {"exc_info": True}
        case other:
            raise Exception("an error in the log")
    _resp = resp
    if type(resp) == BaseModel:
        _resp = resp.model_dump()
    _log(f"{_resp}", extra={
            'caller_path':caller_filename,
            'caller_lineno':caller_lineno
            },
        **other_params if other_params!=None else {}
        )
    return resp

def logResponse(resp:BaseModel | dict):
    return __toLog(logger, resp, 0)

def logInfo(resp:BaseModel | dict):
    return __toLog(logger, resp, 0)

def logDebug(resp:BaseModel | dict):
    return __toLog(logger, resp, 1)

def logError(resp:BaseModel | dict):
    return __toLog(logger, resp, 2)