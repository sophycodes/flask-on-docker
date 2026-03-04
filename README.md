# Flask on Docker [![CI](https://github.com/sophycodes/flask-on-docker/actions/workflows/tests.yml/badge.svg)](https://github.com/sophycodes/flask-on-docker/actions/workflows/tests.yml)

## Overview

This repository demonstrates a production-ready web service built with Flask, PostgreSQL, Gunicorn, and Nginx, all containerized with Docker. The application supports a REST API endpoint, static file serving, and user image uploads. In development, Flask's built-in server is used with a direct port mapping. In production, Gunicorn serves as the WSGI server behind an Nginx reverse proxy, which handles static and media files directly for improved performance.

![Demo](demo.gif)

## Build Instructions

### Development

Build and start the containers:
```
docker compose up -d --build
```

Create the database tables:
```
docker compose exec web python manage.py create_db
```

The app will be available at http://localhost:5743

To upload an image visit http://localhost:5743/upload

To bring down the containers:
```
docker compose down -v
```

### Production

Build and start the production containers:
```
docker compose -f docker-compose.prod.yml up -d --build
```

Create the database tables:
```
docker compose -f docker-compose.prod.yml exec web python manage.py create_db
```

The app will be available at http://localhost:8087

To upload an image visit http://localhost:8087/upload

To view uploaded image visit http://localhost:8087/media/YOUR_IMAGE_FILENAME

To bring down the containers:
```
docker compose -f docker-compose.prod.yml down -v
```

### Note on Ports
This project uses port 5743 (development) and 8087 (production)
to avoid conflicts on a shared server. To use standard ports,
change the port mappings in docker-compose.yml and
docker-compose.prod.yml to 5000:5000 and 80:80 respectively.
