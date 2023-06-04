FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a directory for the app
# RUN mkdir /app
WORKDIR /soils_container
COPY ./requirements.txt /soils_container/requirements.txt

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libgeos-dev \
    libproj-dev \
    gdal-bin \
    libsqlite3-mod-spatialite \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# install dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /soils_container/requirements.txt
# Copy the Django project into the container
COPY . .

# Set up the SQLite database

RUN python manage.py makemigrations

RUN python ./manage.py shell -c "import django;django.db.connection.cursor().execute('SELECT InitSpatialMetaData(1);')";

RUN python manage.py migrate

RUN python manage.py export_or_import_soils "import"

RUN python manage.py admin_default_user

# Expose the port the app runs on

EXPOSE 8004
# Start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]
