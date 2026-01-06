#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field


# Modelo para un Laptop
class Portatil(BaseModel):
    marca: str|None = None
    modelo: str|None = None
    precio: float|None = None
    rating: int|None = None
    marcaprocesador : str|None = None #enum
    modeloprocesador: str|None = None
    numcores: int|None = None
    numthreads: int|None = None
    memoriaram: int|None = None
    tipomemoriaprimaria: str|None = None #enum
    capacidadmemoriaprimaria: int|None = None
    tipomemoriasecundaria: int|None = None #enum
    OS: str|None = None