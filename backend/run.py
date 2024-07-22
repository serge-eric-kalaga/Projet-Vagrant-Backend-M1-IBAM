# from sqlalchemy_utils import create_database, database_exists
# from api.database import engine
from api import createApp, SETTINGS
import logfire
app = createApp(SETTINGS())


    
if __name__ == "__main___":
    import uvicorn
    logfire.configure()
    logfire.instrument_fastapi(app)
    uvicorn.run(app, port=80, host="0.0.0.0")#, proxy_headers=True)#, root_path="/backend_template" )