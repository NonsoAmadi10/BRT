# We Use an official Python runtime as a parent image
FROM python:3.7
WORKDIR /usr/src/app 
ENV PYTHONBUFFERED 1 
# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
