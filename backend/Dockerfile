FROM python:3.10.12-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r /app/requirement.txt

RUN chown www-data:www-data -R /app

RUN chown www-data:www-data -R /app/reports

USER www-data

CMD ["python", "main.py"]