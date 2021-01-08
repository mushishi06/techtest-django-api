# techtest-django-api

REST-based API to be consumed by a remote client

Your API must offer the following capabilities:
1) Register a product
2) Retrieve Product Details from SKU
3) List all available products (&gt;0 Qty)
4) List all sold out products (0 Qty)
5) Register Qty Change (SKU, +/- Value)

Each Product has the following fields:
* SKU `string`, unique
* Name `char255`
* Qty `int32`
* Price `double`

Key Objectives:
1) Consistent in-memory Data Modelling
2) Industry-compliant API REST Endpoints
3) Dockerized environment

Stretch Goals:
1) Automated Testing
2) Documentation
3) Data Persistence


## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/mushishi06/techtest-django-api.git
$ cd techtest-django-api
$ pipenv install
$ pipenv shell
```

3.  Run:

```
(techtest-django-api) $ python manage.py runserver
```
