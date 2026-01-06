from fastapi import APIRouter, HTTPException, FastAPI, Response, status, Body, Query, Path 
from typing import Union, Annotated, Any
from pydantic import Field

from api.data.portatildata import PortatilData
from api.utilidades.models import Portatil

router = APIRouter()

laptop = PortatilData()

#laptops


####GET

#todos
@router.get("/all")
async def laptops_all():
    return await laptop.get_allPortatiles()

#maximo de precio
@router.get("/precio/{precio_laptop}")
async def laptops_max_price(precio_laptop: int):
    return await laptop.get_portatilesPrecioMax(precio_laptop)

#por os
@router.get("/os")
async def laptops_max_price(sistema: str):
    return await laptop.get_portatilesOS(sistema)

#por id
@router.get("/{laptop_id}")
async def laptops_by_id(laptop_id: int):
    return await laptop.get_portatil(laptop_id)

#por query params
@router.get("/")
async def laptops_by_query(skip: int=0, total: int=10, filtronombre: str| None = None):
    return await laptop.get_portatilesModelo(skip=skip, total=total, filtronombre=filtronombre)


##POST portatil

@router.post("/")
async def write_laptop(portatil: Portatil):
    return await laptop.write_portatil(portatil)

##PUT portatil

@router.put("/")
async def update_laptop(portatil:Portatil, laptop_id:int):
    return await laptop.update_portatil(portatil_id=laptop_id, portatil=portatil)


##DELETE portatil

@router.delete("/")
async def delete_laptop(laptop_id: int):
    return await laptop.delete_portatil(laptop_id)







