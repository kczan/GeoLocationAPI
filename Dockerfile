# pull official base image
FROM python:3.8.3-slim-buster

# set work directory
RUN mkdir -p /home/app


# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install system dependencies with OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# copy project
COPY . $APP_HOME

# install project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-dependencies

CMD python manage.py migrate
CMD python manage.py createsuperuser --no-input --username filip --email fc@mail.com --database geolocation --password geolocation
CMD python manage.py collectstatic
CMD gunicorn GeoLocatingAPI.wsgi:application --bind 0.0.0.0:8000

