# Palenca API

This is a dockerized repo using Flask, and MySQL DB

### To run app
```sh
docker-compose up
```
or 
```sh
make up
```

### If database schemas was not created automatically
1. Enter to the docker app container
2. Execute the command ``flask shell``
3. Import packages ``from app.src import db``
4. Create the missing table ``db.create_all()``

### Endpoints
The local host is: localhost:8000

The endpoints are:

* GET '/'

* POST '/uber/register'
params: {"email":"foo", "password":"bar"}

* POST '/uber/login'
params: {"email":"foo", "password":"bar"}

* GET '/profile'
headers: {"Authorization": "Bearer <token>"}

### CURL
Index
```shell
curl --location --request GET 'localhost:8000/'
```

Register
```shell
curl --location --request POST 'localhost:8000/uber/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "pierre@palenca.com",
    "password": "MyPwdChingon123"
}'
```

Login
```shell
curl --location --request POST 'localhost:8000/uber/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "pierre@palenca.com",
    "password": "MyPwdChingon123"
}'
```

Profile
```shell
curl --location --request GET 'localhost:8000/uber/profile' \
--header 'Authorization: Bearer <token>'

```
