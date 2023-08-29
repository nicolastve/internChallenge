from sqlalchemy.orm import Session
from models import Reports
from schemas import GenerateReport, CreateReport
from datetime import datetime

def create_report(db: Session, report: GenerateReport):

    #format dates to datetime
    start= datetime.strptime(report.start_date, '%Y-%m-%d').date()
    end= datetime.strptime(report.end_date, '%Y-%m-%d').date()

    #generate report
    new_report = CreateReport(start_date = start, end_date = end)
    new_report = Reports(**new_report.model_dump())
    
    #add into database
    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    #get current report
    current_report = db.query(Reports.id, Reports.start_date, Reports.end_date, Reports.status).order_by(Reports.id.desc()).first()
    current_report = {
        'id': current_report.id,
        'start_date': datetime.strftime(current_report.start_date, '%Y-%m-%d'),
        'end_date': datetime.strftime(current_report.end_date, '%Y-%m-%d'),
        'status': current_report.status
    }

    return current_report

def get_all_reports(db: Session):
    all_reports = db.query(Reports.id, Reports.start_date, Reports.end_date, Reports.status).order_by(Reports.id.desc()).all()

    keys = ['id', 'start_date', 'end_date', 'status']
    all_reports = [dict(zip(keys, report)) for report in all_reports]

    return all_reports

def get_path(db: Session, id: int):
    report = db.query(Reports.path, Reports.status, Reports.id).filter(Reports.id == id).first()

    if report.status != "Finalized":
        return {'warning': f'report with id {report.id} has not finalized his process'}, False
    
    return report.path, True