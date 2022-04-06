from fastapi import Request, FastAPI
from json import JSONDecodeError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from vehicules import Car, Boat, Motorbike, Plane

app = FastAPI()

#Starting confirmation
@app.get('/')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'info': 'API lancée'})

#Get number vehicules by vehicules
@app.get('/vehicules/cars')
def getNombre():
    return 'Nombre de voitures :', {Car.counter}

@app.get('/vehicules/boats')
def getNombre():
    return 'Nombre de bateaux :', {Boat.counter}

@app.get('/vehicules/motorbikes')
def getNombre():
    return 'Nombre de motos :', {Motorbike.counter}

@app.get('/vehicules/planes')
def getNombre():
    return "Nombre d'avions : ", {Plane.counter}

#Get the number of all the vehicules
@app.get('/vehicules')
def getNombre():
    return "Nombre de véhicules : ", {Plane.counter+Motorbike.counter+Boat.counter+Car.counter}

# if road doesn't exist
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })

