# API Rest Python 

This repo shows how to create a simple Python CRUD application using MySQL and Flask micro web framework.
This application helps you to save deploy events in a MySQL database.
Among the included features, you'll see how to:

* POST a JSON with deploy event information;
* List resources with GET metehod;
* List a especific event passing the event ID in URI;
* DELETE deploys events passing the event ID in URI;

## Locally Requirements
* Docker
* python3
* pip3
* docker-compose
* kubectl 

## Installation guide
##### Clone the repo

```bash
$ git clone 
$ cd Desafio
```

##### Run locally with docker
If you want to run this app locally using Docker, execute the command:
```bash
$ docker-compose up -d
```
After create the containers, acess http://localhost:5000/help to see how to use the API.
In this case we are usin a MySQL server in docker container, if you want to user another MySQL database just change the env vars in `docker-compose.yml` file, pointing to your MySQL server, dont forget to use `app.sql` script to create the application database structure in your database.

##### Run in Kubernetes
```bash
$ kubectl create -f k8s-manifests/
```
After create the service, deployment and MySQL on K8S cluster, get the URL service acess http://urlservice:port/help to see how to use the API.
In this case we are usin a MySQL server in Kubernetes cluster, if you want to user another MySQL database just change the env vars in `k8s-manifests/app-deployment.yml` pointing to your MySQL server, don't forget to use `app.sql` script to create the application database structure in your database.

