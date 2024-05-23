# FastAPI SQL

This API allows you to manage students and courses within a university system.With this API, you can perform CRUD (Create, Read, Update, Delete) operations on students and courses, enabling you to maintain accurate records of enrolled students and available courses.

## Local run

In this api there is requests for READ, ADD, UPDATE and REMOVE from database.
Use the following commands to run the program.

### Installation

```
pip install -r requirements.txt
```

### File structure

For these examples, let's say you have a directory named my_super_project that contains a sub-directory called sql_app with a structure like this:

```
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

The file `__init__.py` is just an empty file, but it tells Python that sql_app with all its modules (Python files) is a package.

Now let's see what each file/module does.

### Create the SQLAlchemy parts

Let's refer to the file sql_app/[database.py](https://github.com/SinaHosseini/PyDeployment/blob/main/1.6.FastAPI%20SQL/expert_app/database.py).<hr>

### Create the database models

Let's now see the file sql_app/[models.py](https://github.com/SinaHosseini/PyDeployment/blob/main/1.6.FastAPI%20SQL/expert_app/models.py).<hr>

### Create the Pydantic models

Now let's check the file sql_app/[schemas.py](https://github.com/SinaHosseini/PyDeployment/blob/main/1.6.FastAPI%20SQL/expert_app/schemas.py).<hr>

### Create the CRUD parts

Now let's see the file sql_app/[crud.py](https://github.com/SinaHosseini/PyDeployment/blob/main/1.6.FastAPI%20SQL/expert_app/crud.py).

In this file we will have reusable functions to interact with the data in the database.

**CRUD** comes from: `Create`, `Read`, `Update`, and `Delete`.<hr>

### Main FastAPI app

And now in the file sql_app/[main.py](https://github.com/SinaHosseini/PyDeployment/blob/main/1.6.FastAPI%20SQL/expert_app/main.py) let's integrate and use all the other parts we created before.<hr>

### Run

- Set `PostgreSQL` database url variable, for example:

```
SQLALCHEMY_DATABASE_URL = "postgresql://sina:ramze_sina@localhost:5432/database_sina"
```

-  Docker pull postgres
```
docker pull postgres
```

- Run `PostgreSQL` docker container, for example:

```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=ramze_sina -e POSTGRES_USER=sina -e POSTGRES_DB=database_sina -d postgres
```

- Database API:

```
uvicorn expert_app.main:app --reload
```

## Liara

Liara's URL is https://sina-docker.liara.run/

You can run the API on [liara.ir](https://console.liara.ir/) :<br>
1 - Set SQLALCHEMY_DATABASE_URL variable<br>
2 - Run the following commnad :

```
liara deploy --platform docker --port 80
```
