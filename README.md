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

## Features

- Django 3.1 and Python 3.7
- [Pipenv](https://github.com/pypa/pipenv) for virtualenvs
- [Docker] soon.

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

## API Details:

In this project you got fiew entries point for `Products`

`GET /api/products/`

* Response: list of ALL products   
>HTTP 200 OK   
>Allow: OPTIONS, GET, POST   
>Content-Type: application/json   
>Vary: Accept   
```JSON
[
    {
        "sku": "UGG-BB-GRE-06",
        "name": "green Ugg boots in the Bailey Bow style, size 6",
        "qty": 0,
        "price": "29.99"
    },
    {
        "sku": "UGG-BB-PUR-06",
        "name": "purple Ugg boots in the Bailey Bow style, size 6",
        "qty": 6,
        "price": "29.99"
    }
]
```


`POST /api/products/`

* request content:
```JSON
{
    "sku": "UGG-BB-Red-06",
    "name": "red Ugg boots in the Bailey Bow style, size 6",
    "qty": 100,
    "price": "29.99"
}
```
* Response: the product created   
>HTTP 201 Created   
>Allow: OPTIONS, GET, POST   
>Content-Type: application/json   
>Vary: Accept   
```JSON
{
    "sku": "UGG-BB-Red-06",
    "name": "red Ugg boots in the Bailey Bow style, size 6",
    "qty": 100,
    "price": "29.99"
}
```


`GET /api/products/UGG-BB-GRE-06/`

* Response: detail of the requested sku   
>HTTP 200 OK   
>Allow: PUT, OPTIONS, DELETE, GET   
>Content-Type: application/json   
>Vary: Accept   
```JSON
{
    "sku": "UGG-BB-GRE-06",
    "name": "green Ugg boots in the Bailey Bow style, size 6",
    "qty": 0,
    "price": "29.99"
}
```


`GET /api/products/sold`

* Response: list of product where qty <= 0   
>HTTP 200 OK   
>Allow: OPTIONS, GET   
>Content-Type: application/json   
>Vary: Accept   
```JSON
[
    {
        "sku": "UGG-BB-GRE-06",
        "name": "green Ugg boots in the Bailey Bow style, size 6",
        "qty": 0,
        "price": "29.99"
    }
]
```


`GET /api/products/available`

* Response: list of product where qty \> 0   
>HTTP 200 OK   
>Allow: OPTIONS, GET   
>Content-Type: application/json   
>Vary: Accept   
```JSON
[
    {
        "sku": "UGG-BB-PUR-06",
        "name": "purple Ugg boots in the Bailey Bow style, size 6",
        "qty": 6,
        "price": "29.99"
    }
]
```


`POST /api/products/qty`

* request content:   
```JSON
{
	"sku": "UGG-BB-GRE-06",
    "qty": -3
}
```
or for positif:   
```JSON
{
	"sku": "UGG-BB-GRE-06",
    "qty": 6
}
```

* Response: full object updated   
>HTTP 200 OK   
>Allow: OPTIONS, POST   
>Content-Type: application/json   
>Vary: Accept   
```JSON
{
    "sku": "UGG-BB-GRE-06",
    "name": "green Ugg boots in the Bailey Bow style, size 6",
    "qty": 0,
    "price": "29.99"
}
