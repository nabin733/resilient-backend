# Resilient NZ — Backend API

Django REST Framework backend for Resilient NZ, providing shelter data and receiving emergency check-ins from the mobile app.

## Features

- REST API for civil defence shelter data (CRUD via Django admin + API)
- Endpoint for receiving offline-queued emergency check-ins from the mobile app
- PostgreSQL database

## Tech Stack

- Python 3.13 / Django 6
- Django REST Framework
- PostgreSQL

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| /api/shelters/ | GET | List all shelters |
| /api/shelters/ | POST | Create a shelter |
| /api/checkins/ | GET | List received check-ins |
| /api/checkins/ | POST | Submit a check-in (used by the mobile app) |
| /admin/ | — | Django admin panel |

## Getting Started

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

## Mobile App

This backend is designed to work with the companion mobile app: https://github.com/nabin733/resilient-nz
