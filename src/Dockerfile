FROM python
WORKDIR /app
RUN apt update -y
RUN apt install watchman -y
COPY app/requirements.txt .
COPY .. .
RUN pip install -r requirements.txt

CMD ["uwsgi", "--socket", ":8000", "--module", "nfuunit.wsgi:application", "--master", "--enable-threads", "--threads", "2"]