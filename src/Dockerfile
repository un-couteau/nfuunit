FROM python
WORKDIR /app
RUN apt update -y
RUN apt install watchman -y
COPY app/requirements.txt .
COPY .. .
RUN pip install -r requirements.txt
