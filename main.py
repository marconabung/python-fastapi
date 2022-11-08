from fastapi import FastAPI, Request, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from models.tbl_users import User
from controllers.templates import templates
from controllers.oauth2 import get_current_user
from configs.db import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI( # API Docs
    title='FastAPI', # app name
    description='Powered by FastAPI',
    version='1.0.1',
    docs_url="/api/docs",
    redoc_url="/api/redocs",
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
        
    openapi_schema = get_openapi(
        title="FastAPI Template OpenAPI",
        version='1.0.1',
        description="Custon OpenAPI schema",
        routes=app.routes
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# CUSTOM ERROR HANDLER FOR FORBIDDEN AND NOT FOUND RESPONSES
# @app.exception_handler(StarletteHTTPException)
# async def custom_404_handler(request: Request, exc: StarletteHTTPException):
#     if exc.status_code == 404:
#         return templates.TemplateResponse("notfound.html", {"request": request, "logged": True})

#     return templates.TemplateResponse("notfound.html", {"request": request, "logged": False})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)