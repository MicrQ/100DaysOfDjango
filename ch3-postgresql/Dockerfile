#Pull base image
FROM python:3.10.4-slim-bullseye


# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
#Disable pip version check everytime
ENV PYTHONDONTWRITEBYTECODE 1
#Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED 1
#Prevent Docker from buffering stdout and stderr

# Set work directory
WORKDIR /100DaysOfDjango

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .