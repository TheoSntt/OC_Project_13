# pull the official base image
FROM python:3.10.11-alpine

# set work directory
WORKDIR /usr/src/app

# ENVIRONMENT VARIABLES
# Prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures that Python output is logged to the terminal.
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Copy project's code into work directory
COPY . /usr/src/app

# Exposes port 8000
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]