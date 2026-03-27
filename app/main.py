from fastapi import FastAPI
from app.routes import router

app = FastAPI() # Creating app instance

app.include_router(router) # Including the router from the routers module to handle API endpoints

