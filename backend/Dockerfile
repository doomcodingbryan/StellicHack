# Dockerfile

# use light python image
FROM python:3.11-slim

# prevent .pyc files to disk in container
ENV PYTHONDONTWRITEBYTECODE = 1
# immediately print terminal outputs without buffering
ENV PYTHONUNBUFFERED = 1

# set working directory as backend
WORKDIR /backend

# need to install system libraries for psycopg2, and delete setup cache to stay lightweight
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# copy requirements into the container
COPY requirements.txt . 

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy backend directory into the container
COPY . . 

# declare the listening port
EXPOSE 8080

# launch uvicorn strictly in the docker container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
