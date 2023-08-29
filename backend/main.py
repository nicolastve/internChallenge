import time
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Reports, EntryMarks, ExitMarks, User
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import landscape


def get_user_entries(db: Session, start_range, end_range):
    results = db.query(User.dni, User.name, User.last_name, EntryMarks.date, EntryMarks.time, ExitMarks.time).\
        join(EntryMarks, User.id == EntryMarks.user_id).\
        join(ExitMarks, User.id == ExitMarks.user_id).filter(
        EntryMarks.date == ExitMarks.date,
        EntryMarks.date >= start_range,
        EntryMarks.date <= end_range
        ).all()

    return results

def generate_report(db: Session):
    while True:
        all_reports = db.query(Reports).filter(Reports.status == 'Generated').all()
        if all_reports:    
            for r in all_reports:
                
                r.status = "Processing"
                db.add(r)
                db.commit()
                db.refresh(r)

                report = get_user_entries(db, r.start_date, r.end_date)
                report = [list(item) for item in report]
                report.insert(0, ['dni', 'name', 'last_name', 'date', 'entry', 'exit'])

                report_name = f'report_from_{r.start_date}_to_{r.end_date}.pdf'

                doc = SimpleDocTemplate(f"./reports/{report_name}", pagesize=landscape(letter))

                # Crear una tabla y definir su estructura
                table = Table(report)
                table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)]))

                # Agregar la tabla al documento
                story = []
                story.append(table)
                doc.build(story)
                

                r.status = 'Finalized'
                r.path = f'\\reports\\{report_name}'
                db.add(r)
                db.commit()
                db.refresh(r)
                db.close()
        else:
            print('There are no reports to be generated')
            db.close()

        time.sleep(5)
            

if __name__ == "__main__":

    db = SessionLocal()
    generate_report(db)