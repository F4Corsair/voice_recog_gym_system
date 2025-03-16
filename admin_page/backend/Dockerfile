FROM python:3.11

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./init.sql /docker-entrypoint-initdb.d/

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]