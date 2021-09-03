# django_with_docker

Testing django with docker

# Prerequisite
1. `Python >= 3`
2. `Docker`
3. `pip` python package manager
4. `git` (not mandatory but `required to clone the repo` || `maybe just download the repo to your system`)

# Steps
1. clone the repo (if you have git) || download the repo (if you don't have git).
2. Open your terminal and cd (change directory) to the repo root.
3. make sure your `docker` && `docker-compose` are installed correctly. (run `docker --version && docker-compose --version` terminal and make sure no error occurs)
4. make sure your `docker desktop` is running.
5. run command ` docker-compose run web django-admin startproject {your_project_name} . ` '.' in the end is mandatory, 'your_project_name' should not contain spaces and '-'(dash).
6. run command ` docker-compose up `
7. open http://localhost:8000

# Add new app to project
1. make sure your command ` docker-compose up ` is up and running.
2. open up a new terminal and run command ` docker ps `. (Displays a list of docker containers currently running)
3. Find the name of the docker container that you want to add a new app to. (something like `*_web_*`)
4. Run command ` docker exec {*_web_*} python manage.py startapp {app_name}`.

**Note:**
you don't need to navigate to your project folder. But it's recommended not to exec any command outside of the project folder.