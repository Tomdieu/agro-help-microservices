FROM python:3.8-slim-buster

EXPOSE 8001

# Set Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Create a directory for the app
WORKDIR /forum_service
COPY ./requirements.txt /forum_service/
RUN python -m pip install --upgrade pip \ 
    && python -m pip install -r /forum_service/requirements.txt
COPY . .

# Copy requirements file and install dependencies

# RUN python manage.py makemigrations && python manage.py migrate

CMD [ "python","manage.py","runserver","0.0.0.0:8005" ]