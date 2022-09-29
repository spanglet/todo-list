# To-Do App

This project runs a single-page application To-Do list, with a separate front- and back-end.

The frontend was created using the Vue.js (v3) Javascript framework. The frontend consumes the
API of the backend, which runs on the Python-base Flask web framework. Persistent storage of data
is held in a MySQL database, which the backend performs operations on and sends to the frontend via
its API in JSON-format.

## Run the App Locally

The To-Do App is run using docker-compose, which creates three containers (mySQL database, Flask backend, Vue.js fronted).

Once the repository is pulled, run the following to build and run the Docker containers:

```
$ docker-compose up --build

```
By default, the website is accessible locally at *127.0.0.1:3000*, assuming port 3000 is not in use

The backend container is rooted at *127.0.0.1:5000*.

