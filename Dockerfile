FROM python:3.11.5
WORKDIR /application
COPY . /application
CMD ["python","application.py"]