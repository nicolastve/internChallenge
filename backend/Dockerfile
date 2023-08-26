FROM python:3.10.12-slim-bullseye

WORKDIR /code

COPY ./requirement.txt /code/requirement.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirement.txt

COPY ./app /code/app

RUN chown www-data:www-data -R /code/app

USER www-data

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]