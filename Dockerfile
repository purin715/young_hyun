FROM python:3.9.0

WORKDIR /home/

RUN echo 'adsfasdf'

RUN git clone https://github.com/purin715/young_hyun.git

WORKDIR /home/young_hyun/

RUN echo "SECRET_KEY = django-insecure-w(m=sj2#^drhzqfdm3$dg4ubcz)vmp6-qetdihe$^$e=$%up7x" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=young_hyun.settings.deploy && python manage.py collectstatic --noinput --settings=young_hyun.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=young_hyun.settings.deploy young_hyun.wsgi --bind 0.0.0.0:8000"]