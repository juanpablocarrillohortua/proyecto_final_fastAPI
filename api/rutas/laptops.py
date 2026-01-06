from fastapi import APIRouter, HTTPException, Body, Query, Path 
from typing import Union, Annotated, Any
from pydantic import Field

from api.data.portatildata import PortatilData
from api.utilidades.models import Portatil, OpSys

router = APIRouter()

laptop = PortatilData()

#laptops


####GET

#todos
@router.get("/all", description="obtener todas las laptops", summary="obtenga cada laptop")
async def laptops_all():
    return await laptop.get_allPortatiles()

#maximo de precio
@router.get("/precio/{precio_laptop}", description="ingrese el precio que desea como tope", summary="obtener las laptops menores a un precio")
async def laptops_max_price(precio_laptop: int = Path(gt=0)): #precio mayor a 0
    res = await laptop.get_portatilesPrecioMax(precio_laptop)

    if len(res['portatiles']) == 0:
        raise HTTPException(status_code=404, detail="Laptop price not found")
    
    return res

#por os
@router.get("/os", description="ingrese el sistema operativo que desea buscar", summary="obtener las laptops con cierto OS")
async def laptops_max_price(sistema: OpSys):
    return await laptop.get_portatilesOS(sistema)

#por id
@router.get("/{laptop_id}", description="ingrese el id del dispositivo", summary="obtener las laptops por su id")
async def laptops_by_id(laptop_id: int = Path(gt=0)): #id mayor a 0
    res = await laptop.get_portatil(laptop_id)
    if not res:
        raise HTTPException(status_code=404, detail="Laptop id not found")
    
    return res

#por query params
@router.get("/", 
            description="skip define en que pos inicia, total cuantas desea extraer y filtronombre permite filtrar segun nombre de modelo", 
            summary="obtener una lista de laptops")
async def laptops_by_query(skip: int=0, total: int=10, filtronombre: str| None = None): #filtro nombre opcional
    return await laptop.get_portatilesModelo(skip=skip, total=total, filtronombre=filtronombre)


##POST portatil

@router.post("/", description="ingrese en el body el formato que se le sugiere abajo (para mas info de este consulte Shemas Portatil)", summary="agregar laptops")
async def write_laptop(portatil: Portatil):
    return await laptop.write_portatil(portatil)

##PUT portatil

@router.put("/", description="ingrese el id del dispositivo que desea actualizar y los campos que desea modificar", summary="actualizar las laptops por su id")
async def update_laptop(portatil:Portatil, laptop_id:int):
    res = await laptop.update_portatil(portatil_id=laptop_id, portatil=portatil)

    if not res:
        raise HTTPException(status_code=404, detail="Laptop id not found")

    return res


##DELETE portatil

@router.delete("/", description="ingrese el id del dispositivo que desea borrar", summary="eliminar las laptops por su id")
async def delete_laptop(laptop_id: int):
    res = await laptop.delete_portatil(laptop_id)

    if not res:
        raise HTTPException(status_code=404, detail="Laptop id not found")
    return res







