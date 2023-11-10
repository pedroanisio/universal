## DJANGO Project Overview

The project incorporates PostgreSQL with Geospatial GIS to manage polygons symbolizing addresses and areas of interest. The PostgreSQL version specified for this project is:

```docker
services:
  db:
    image: postgis/postgis:16-3.4
```

In terms of database design, there's an adoption of UUIDs over bigint IDs to bolster security. The implementation in Django is as follows:


```python
from django.db import models
import uuid

# Base model for using UUID as the primary key
class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

# Sample Person model inheriting from UUIDModel
class Person(UUIDModel):
```

The project employs django-rest-framework to facilitate API development. The APIs are associated with a variety of models, including:
- Person
- Address
- AddressHistory
- EmailAccount
- EmailHistory
- MobileAccount
- MobileHistory
- PersonalDocument
- Region

## Project Directory Structure

The organization of the project's directories is as follows:

```
django_project/
├── tests/
├── personal/ # Main project application
│   └── api/
├── docker-compose.yaml
├── Dockerfile
└── manage.py
```

## Development Environment

The project's development environment is configured using Docker.

## Operational Scripts

### Dropping the Environment

To drop the environment, execute the following commands:

```shell
docker compose up -d                                
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### Building the Development Environment

To build the development environment, use the same set of commands:

```shell
docker compose up -d                                
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

## Test

```shel
docker compose exec web python manage.py test --debug-mode
```

## Docker compose

```yaml
version: "3.12"
services:
  db:
    image: postgis/postgis:16-3.4
    restart: always
    environment:
      POSTGRES_DB: universal
      POSTGRES_PASSWORD: password
      
  web:
    build: .
    restart: always
    ports:
      - "8000:8000"
    depends_on:
      - db
    volumes:
      - .:/app

```