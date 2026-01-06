from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


from api.docs import tags_metadata
from api import PortatilData
from api import laptop_router

laptop = PortatilData()

app = FastAPI(title="Api Laptops",
              version="0.0.2",
              description="una ApiRestfull para gestion del crud de laptops",
              contact={
                  "name":"Juan Pablo",
                  "url":"https://github.com/juanpablocarrillohortua"
              },
              license_info={
                  "name":"Apache 2.0",
                  "url":"https://www.apache.org/licences/LICENCE-2.0.html"
              },
              openapi_tags=tags_metadata
              )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.exception_handler(RequestValidationError)
async def http_exception_handler(request, exc):
    error = exc.errors()[0]
    
    field = error.get("loc")[-1] 
    msg = error.get("msg")
    
    return JSONResponse(
        status_code=422,
        content={"error": f"Error en el campo '{field}': {msg}"}
    )



app.include_router(laptop_router, prefix="/laptop", tags=['Laptops'])

