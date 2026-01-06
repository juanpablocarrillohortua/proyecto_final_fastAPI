#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field

class ProccesorBrand(str, Enum):
    intel = "intel"
    amd = 'amd'
    apple = 'apple'
    other = 'other'

class TypeMemory(str, Enum):
    SSD = 'SSD'
    HDD = 'HDD'

class TypeMemorySec(str, Enum):
    SSD = 'SSD'
    HDD = 'HDD'
    No_secondary_storage = 'No secondary storage'

class OpSys(str, Enum):
    windows = 'windows'
    mac = 'mac'
    dos = 'dos'
    android = 'android'
    chrome = 'chrome'
    other = 'other'
    ubuntu = 'ubuntu'


# Modelo para un Laptop
class Portatil(BaseModel):
    marca: str|None = None
    modelo: str|None = None
    precio: float|None = None
    rating: int|None = None
    marcaprocesador : ProccesorBrand|None = None 
    modeloprocesador: str|None = None
    numcores: int|None = None
    numthreads: int|None = None
    memoriaram: int|None = None
    tipomemoriaprimaria: TypeMemory|None = None
    capacidadmemoriaprimaria: int|None = None
    tipomemoriasecundaria: TypeMemorySec|None = None 
    OS: OpSys|None = None 