# 20260601-DE5M5

Scenario:

User Stories or Backlog:

Solutions Diagram:
Hint - Use something like draw.io and add the image into this ReadMe.md file. 


# PM Task

1. Load the two datasets
2. Clean the them (thoroughly)
3. Measure at least 1 data engineering metric in the data cleaning process (ie dropped rows)
4. MVP: Output the cleaned files as a local csv.

Stretch: 

5. Output the cleaned files into the local SSMS (use SQLAlchemy); create a new DB for this.
6. Refactor your code into modular functions.

# Day 2

## AM Task:

- Focus on having at least one function like:
    - dataEnrich():
        - Calculate the days between the two date columns and add it as a new col. 
    - fileLoader
    - duplicateCheck
    - naCheck
    - dataCleaner
    - addToSQL

# Day 3: Airflow YAML
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5

  airflow:
    image: apache/airflow:2.9.3-python3.11
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
      _AIRFLOW_DB_MIGRATE: 'true'
      _AIRFLOW_WWW_USER_CREATE: 'true'
      _AIRFLOW_WWW_USER_USERNAME: admin
      _AIRFLOW_WWW_USER_PASSWORD: admin
    volumes:
      - ./dags:/opt/airflow/dags
    ports:
      - "8080:8080"
    command: standalone


