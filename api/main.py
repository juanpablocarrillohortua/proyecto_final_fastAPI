from fastapi import FastAPI


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


app.include_router(laptop_router, prefix="/laptop", tags=['Laptops'])

