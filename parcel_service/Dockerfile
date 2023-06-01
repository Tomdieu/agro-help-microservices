FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set the working directory
WORKDIR /parcel

COPY requirements.txt ./

# # install dependency

RUN pip install -r requirements.txt

COPY . .


EXPOSE 8003