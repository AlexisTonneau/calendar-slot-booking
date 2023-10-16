from fastapi import FastAPI
import uvicorn as uvicorn
from uvicorn.config import LOGGING_CONFIG
import os

from config.service_loader import init_services


app = FastAPI()

services = init_services()


@app.get("/")
async def root():
    return {"message": services.hello_service.get_message()}



if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')) or 9000)
