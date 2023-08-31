FROM python:3.10.12-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r /app/requirement.txt

EXPOSE 8000

RUN chown www-data:www-data -R /app

RUN chown www-data:www-data -R /app/reports

USER www-data

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]