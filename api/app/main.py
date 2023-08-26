from fastapi import FastAPI
import requests

app = FastAPI()
url_backend = 'http://backend:8001/version'

@app.post('/generate')
async def generate_report():
    return {'message':'report generated'}

@app.get('/download')
def download_report():
    return {'message': 'success'}

@app.get('/version_backend')
def version_backend():
    result = requests.get(url_backend)
    return result.text