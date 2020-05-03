# sample-airflow-docker-compose

Sample Docker Compose files for [Airflow docker image](https://hub.docker.com/r/apache/airflow).

It is supposed to be used for a personal development environment.


## Usage

- (1) Copy env files from sample files

```sh
cp docker-compose/sample-airflow.env docker-compose/airflow.env 
cp docker-compose/sample-airflow-backend.env docker-compose/airflow-backend.env 
```

- (2) Edit the env files (or you can also use it as is)

- (3) Run `docker-compose up`

```sh
docker-compose -p airflow-local -f docker-compose/airflow.yml -f docker-compose/airflow-backend.yml up -d
```

- (4) Wait for launching Airflow (Check Docker logs see if there are any problem)

```sh
docker-compose -p airflow-local -f docker-compose/airflow.yml -f docker-compose/airflow-backend.yml logs
```

- (5) Open `http://localhost:8080` and try Airflow

- (6) Finish Airflow sample

```sh
docker-compose -p airflow-local -f docker-compose/airflow.yml -f docker-compose/airflow-backend.yml down
```

