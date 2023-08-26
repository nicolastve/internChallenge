from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

allowed_service = 'backend'

@app.middleware('http')
async def check_ip(request: Request, call_next):
    # Obtener el nombre del servicio del encabezado de la solicitud
    service_name = request.headers.get("X-Service-Name")

    # Verificar si el servicio tiene permiso para acceder
    if service_name != allowed_service:
        raise HTTPException(status_code=403, detail="Acceso denegado")

    response = await call_next(request)
    return response

@app.post('/generate')
async def generate_report():
    return {'message': 'Requests sent'}

@app.get('/version')
def version_backend():
    return {'version': 1.0}
