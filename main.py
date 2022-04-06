from fastapi import Request, FastAPI
from json import JSONDecodeError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from vehicules import Car, Boat, Motorbike, Plane

app = FastAPI()

@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'info': 'API lancée'})


@app.get('/vehicules/cars')
def getNombre():
    return 'Nombre de voitures :',{Car.counter}

@app.get('/vehicules/boats')
def getNombre():
    return 'Nombre de bateaux :',{Boat.counter}

@app.get('/vehicules/motorbikes')
def getNombre():
    return 'Nombre de motos :',{Motorbike.counter}

@app.get('/vehicules/planes')
def getNombre():
    return "Nombre d'avions : ",{Plane.counter}







@app.get('/')
def getinformation():
    return True

@app.get('/ifa/user/{id}')
def getUser(id: int):
    print(f"l'id est le suivant {id}")
    return {'userpage': True}


# if road doesn't exist
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })

