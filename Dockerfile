# pull base image
FROM continuumio/miniconda3

ENV APP_HOME /campbell
WORKDIR $APP_HOME
COPY . $APP_HOME

# set work directory
# WORKDIR /campbell

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# prepare the environment
RUN conda update --name base conda &&\
    conda env create --file environment.yaml
SHELL ["conda", "run", "--name", "campbell", "/bin/bash", "-c"]

# collect static files
# RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn campbell.wsgi:application --bind 0.0.0.0:$PORT
