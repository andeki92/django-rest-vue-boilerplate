<h1 align="center">
    <!-- <br>
        <a href="#">
            <img src="" alt="dashboard" width="200"/>
        </a>
    <br> -->
        DjangoREST-Vue-Boilerplate
    <br>
</h1>

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-vue.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com)

A full stack boilerplate using a dockeriside Django-REST backend and a Vue.js frontend

<details>

<!-- toc -->

- [Configuration](#configuration)
- [Development](#development)
- [Credits](#credits)
- [License](#license)

<!-- tocstop -->

</details>

# Configuration

To start using the boilerplate, you need to have the following installed:

- [Docker CE](https://docs.docker.com/install/) - This is used to containerise the Django application
- [Node.js](https://nodejs.org/en/)
- [Python3](https://python.org/en)

## Backend

Once installed you need to set up your environment file. `./system-backend/config/.env`. The PostgreSQL database name, username and password will be the login credentials needed to access the Postgres Database and the Django application will also use these to have read/write access. To generate a new `DJANGO_SECRET_KEY` you can run the following command:

```
$ python3 -c 'import secrets; print(secrets.token_hex(50))'
```

Once you've saved the `.env` file (remember to NEVER commit this to git), you can start the containers by running the following (you might need to run these using **sudo**):

```
$ docker-compose build
```

This will download all the dependencies and load them into docker. To get the database configured properly, simply run:

```
$ docker-compose run web python manage.py makemigrations
$ docker-compose run web python manage.py migrate
```

Your Django application should now be ready to be launched in your dev environment. To be able to login however you need to create a user, do this by with:

```
$ docker-compose run web python manage.py createsuperuser
```

🔥 **THAT'S IT** - You're done configuring the backend application (at least for now). Either continue to configure the frontend-application or look at the [Development Section](#development) for instructions on how to run your application.

## Frontend

🧐 This seems oddly empty...

# Development

The following section explains how to run your application along with some useful commands that can help developing your own application.

## Backend

In order to start your development environment you simply need to tell Docker-Compose to spin up your containers (again, you might need to run these with **sudo**):

```
$ docker-compose up
```

If you feel the constant terminal spamming is a bit over the top, you can start it as a background process:

```
$ docker-compose up -d
```

To stop all running containers:

```
$ docker-compose down
```

Once _composed_ your Django application will be available on http://localhost:8080. If you navigate to http://localhost:8080/admin you should be able to log in using the credentials we created in the [Configuration Section](#Configuration)

## Frontend

🧐 Still empty... maybe consider adding information here?
