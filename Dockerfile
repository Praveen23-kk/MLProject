FROM python:3.7-slim-buster 
WORKDIR /app
COPY . /app

RUN apt update -y && apt requirements.txt

RUN pip install -r requirements.txt
CMD ["python3","app.py"]