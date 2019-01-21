# Falcon small app

## About this project

Small project to test the Falcon library. 

## Technology used

* [Falcon](https://falcon.readthedocs.io/en/stable/) - Python Library to create API's
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper
* [Docker](https://www.docker.com/) - Tool designed to make it easier to create, deploy, and run applications by using containers

## How to run this app (Docker)

To run this project you need to have Docker installed, you can get it from [here](https://www.docker.com/products/docker/)

Documentation about Docker can be found [here](https://docs.docker.com/)

Check you have docker installed and running by running this command `docker info`

If you get this message:

*[Error response from daemon: Bad response from Docker engine]*

docker is not running.

If not, go inside the project and run `docker-compose -f docker-compose-dev.yml up`
The first time will take a while, docker is downloading everything he needs to run the project, be patient.


## How to hit the endpoints

***Note replace data with the values you want.

**Create a patient**

`
curl --request POST \
  --url http://127.0.0.1:8000/patients \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9zZWciLCJwd2QiOiJwYXNzd29yZCJ9.9pkUP_tW9Ct27w0VNit6Oo62FKhsCksNNoHFmj2KQBk' \
  --header 'content-type: application/json' \
  --data '{
	"first_name": "FirstName",
	"last_name": "LastName",
	"birth_date": "1992-01-01"
}'
`


**List patients**

`
curl --request GET \
  --url 'http://127.0.0.1:8000/patients?__offset=0&__limit=10' \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9zZWciLCJwd2QiOiJwYXNzd29yZCJ9.9pkUP_tW9Ct27w0VNit6Oo62FKhsCksNNoHFmj2KQBk'
`


**Create an appointment**

`
curl --request POST \
  --url http://127.0.0.1:8000/appointments \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9zZWciLCJwd2QiOiJwYXNzd29yZCJ9.9pkUP_tW9Ct27w0VNit6Oo62FKhsCksNNoHFmj2KQBk' \
  --header 'content-type: application/json' \
  --data '{
	"patient_id": 1,
	"date": "2019-01-23"
}'
`


**List appointments**

`
curl --request GET \
  --url http://127.0.0.1:8000/appointments \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9zZWciLCJwd2QiOiJwYXNzd29yZCJ9.9pkUP_tW9Ct27w0VNit6Oo62FKhsCksNNoHFmj2KQBk'
`

## Runnning tests

`docker-compose -f docker-compose-dev.yml exec ccm pytest --disable-warnings`


