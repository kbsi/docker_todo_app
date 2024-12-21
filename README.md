# TP Docker - BOULAIS KEVIN

## How to get and launch the project ?

To get the project from GitHub and execute the Docker Compose, follow these steps:

1. Clone the repository:

```sh
git clone https://github.com/kbsi/docker_todo_app.git
```

2. Navigate to the project directory:

```sh
cd docker_todo_app
```

3. Build and start the Docker containers:

```sh
docker-compose up
```

This will download the necessary images, build the containers, and start the application.

4. Access the application:

   - The backend service will be available at `http://localhost/api`.
   - The frontend service will be available at `http://localhost`.
   - phpMyAdmin will be available at `http://localhost:8081`. user root and password root

## What do you find in the docker compose file?

The `docker-compose.yml` file is used to define and run multi-container Docker applications. It allows you to configure your application's services, networks, and volumes in a single file. By using `docker-compose up`, you can start and run your entire application with a single command. This file typically includes details such as the images to use, environment variables, ports to expose, and dependencies between services.

### Services Defined

- **mysql**: A MySQL database service.
- **backend**: A Flask backend service.
- **frontend**: An Angular frontend service.
- **phpmyadmin**: A phpMyAdmin service for database management.
- **nginx**: An Nginx proxy service.

### Dependencies Between Services

The services defined in the `docker-compose.yml` file often have dependencies on each other. For example, the `backend` service depends on the `mysql` service to access the database. Similarly, the `frontend` service may depend on the `backend` service to fetch data. The `nginx` service acts as a reverse proxy, routing requests to the appropriate `frontend` or `backend` services. The `phpmyadmin` service depends on the `mysql` service to manage the database.

### Volumes

- `dbdata`: A named volume for persisting MySQL data.

### Networks

- `app-network`: A custom network for inter-service communication.

## Nginx Proxy Configuration

The `nginx/nginx.conf` file configures Nginx as a reverse proxy for your application. Below is an explanation of the configuration:
