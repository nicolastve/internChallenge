from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import GenerateReport
from crud import create_report, get_all_reports, get_path

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/generate')
async def generate_report(report: GenerateReport, db: Session = Depends(get_db)):
    new_report = create_report(db, report)
    return new_report

@app.get('/all_reports')
def get_reports(db: Session = Depends(get_db)):
    all_report = get_all_reports(db)
    return all_report
    
@app.get('/download')
def download_report(id: int, db: Session = Depends(get_db)):
    path, status = get_path(id=id, db=db)

    if status:
        return FileResponse(path, filename="reporte.pdf", headers={"Content-Disposition": "attachment"})
    return path