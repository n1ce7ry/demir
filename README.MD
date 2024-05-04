![Static Badge](https://img.shields.io/badge/python-3.12-green)
![Static Badge](https://img.shields.io/badge/django-5.0.4-blue)
<img alt="GitHub" src="https://img.shields.io/github/license/n1ce7ry/SyncPro">

# Demir     

Demir - Exclusive Car Rental

Welcome to Demir, a premium portal for exclusive car rentals. We offer you the opportunity to drive your dreams with our luxury cars available for rent for any length of time.

## Quick start

Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Clone the project
```bash
https://github.com/n1ce7ry/demir
```

Install the dependencies
```bash
poetry shell
poetry install
```

Edit env.example, rename it to env.sh, and run it:
```bash
vim env.example
mv env.example env.sh
./env.sh
```

Apply migrations
```bash
./manage.py migrate
```

Run server 
```bash
./manage.py runserver
```
