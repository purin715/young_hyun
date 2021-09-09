FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/purin715/young_hyun.git

WORKDIR /home/young_hyun/

RUN echo "SECRET_KEY = django-insecure-w(m=sj2#^drhzqfdm3$dg4ubcz)vmp6-qetdihe$^$e=$%up7x" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "young_hyun.wsgi", "--bind", "0.0.0.0:8000"]