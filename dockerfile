FROM python:3.11-slim

WORKDIR /fullapp

COPY ./frontend /fullapp

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]
