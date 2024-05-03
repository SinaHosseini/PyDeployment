# FastAPI

Write `GET`, `POST`, `PUT` and `DELETE` requests.

## ToDo App

In this api there is requests for read, add, update and remove database

## Image-based API

In this api there is face analysis is done, such as age, gender and race, just send a photo file and see the result

## Installation

The easiest way to install libraries is run this command:

```
pip install -r requirements.txt
```

<hr>
Use the following commands to run the program.<br>
Database API:

```
uvicorn database_API:app --reload
```

<hr>

Deep Face:

```
uvicorn main:app --reload
```
