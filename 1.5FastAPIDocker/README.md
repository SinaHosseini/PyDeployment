# Fast API | Docker

I'll show you how to build a **Docker** image for **FastAPI** from scratch, based on the official Python image.

## ToDo App

In this api there is requests for `READ`, `ADD`, `UPDATE` and `REMOVE` from database.<br>
Use the following commands to run the program.
Database API:

```
uvicorn main:app --reload
```

## Build Docker

The most common way to do it is to have a file requirements.txt with the package names and their versions, one per line.

```
pip install -r requirements.txt
```

<strong>Create the FastAPI Code</strong><br><hr>

- Create an `app` directory and enter it.<br>
- Create a [`main.py`](https://github.com/SinaHosseini/PyDeployment/blob/1241c133a2705531bc2ab283655c1c494222dfcf/1.5FastAPIDocker/app/main.py) file.

<strong>DockerFile</strong><br><hr>
Now in the same project directory create a file [`Dockerfile`](https://github.com/SinaHosseini/PyDeployment/blob/4e50ed613a7b8b36830d7a54f275f1ab76a26be2/1.5FastAPIDocker/Dockerfile)

<strong>Build the Docker Image</strong><br><hr>
Now that all the files are in place, let's build the container image.

- Go to the project directory (in where your `Dockerfile` is, containing your `app` directory).
- Build your FastAPI image:

```
docker build -t myimage .
```

<strong>Start the Docker Container</strong><br><hr>

- Run a container based on your image:

```
docker run -d --name mycontainer -p 80:80 myimage
```

<strong>Interactive API docs</strong><br><hr>
Now you can go to http://192.168.99.100/docs or http://127.0.0.1/docs (or equivalent, using your Docker host).

You will see the automatic interactive API documentation (provided by Swagger UI):<br>
![img](images/img1.jpg)<br><br>
<strong>Alternative API docs</strong><br><hr>
And you can also go to http://192.168.99.100/redoc or http://127.0.0.1/redoc (or equivalent, using your Docker host).

You will see the alternative automatic documentation (provided by ReDoc):
![img2](images/img2.png)

## Docker command
Docker commands can be followed from the link below:<br>
[Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)