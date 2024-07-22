from fastapi import APIRouter, Depends
from api.schemas.response import Response
from api.database import get_db, Session

healthcheck_router = APIRouter(tags=['HEALTHCHECK'])


@healthcheck_router.get("/", status_code=200, response_model=Response[str])
def verifyHealth(db:Session = Depends(get_db)):
    return Response(status=1, message="OKAY")
