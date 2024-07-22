from api.configs import SETTINGS
from pydantic_settings import BaseSettings
from fastapi import FastAPI

def createApp(config:BaseSettings) -> FastAPI:
	from api.configs.config import Setting
	Setting = config
	import werkzeug.exceptions as werkexcept
	from fastapi import Request, HTTPException
	from fastapi.middleware.cors import CORSMiddleware
	from fastapi.exceptions import RequestValidationError
	from fastapi.responses import JSONResponse, StreamingResponse
	from starlette.exceptions import HTTPException as starletteHTTPException
	# from api.services import socket
	from api.utility.lifespan import LifeSpan
	from api.configs.logging import logDebug, logInfo, logError
	from api.views.tasks import router as tasks_router
	

	app = FastAPI(
		lifespan=LifeSpan,
	)

	app.include_router(tasks_router, prefix="/api/tasks", tags=['TASKS'])


	#------get request from any webpage---------
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)
	#--------add logger for each an every request--------
	@app.middleware("http")
	async def loggingRequest(request:Request, call_next):
		logDebug(f"-------------------------------------------------------------------------")
		logInfo(f"{request.method}, {request.url}, {request.client.host}")
		response:StreamingResponse = await call_next(request)
		logInfo(f"{response.status_code}")
		return response

	@app.exception_handler(werkexcept.HTTPException)
	def handleWerkZeugException(req, exc):
		logError(exc)	
		return JSONResponse(content={"status":-1, "message":f"{exc.description}"}, status_code=exc.code)

	@app.exception_handler(HTTPException)
	def handleHTTPException(req, exc):
		logError(exc)	
		return JSONResponse(content={"status":-1, "message":f"{exc.detail}"}, status_code=exc.status_code)

	@app.exception_handler(RequestValidationError)
	def handleValidationErrorException(req, exc):
		logError(exc)	
		return JSONResponse(content={"status":-1, "message":f"{exc}"}, status_code=400)

	@app.exception_handler(starletteHTTPException)
	def handleStarletteException(req, exc):
		logError(exc)	
		return JSONResponse(content={"status":-1, "message":f"{exc.detail}"}, status_code=exc.status_code)

	@app.exception_handler(Exception)
	def handleException(req, exc):
		logError(exc)	
		return JSONResponse(content={"status":-1, "message":f"{exc}"}, status_code=500)

	#----------------init db------------------
	from api.database import init_database, engine
	init_database(engine)
	return app

