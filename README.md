# Meetups project

Creating Meetups project with django and docker

# Prerequisite
1. `Python >= 3`
2. `Docker`
3. `pip` python package manager
4. `git` (not mandatory but `required to clone the repo` || `maybe just download the repo to your system`)

# Steps
1. clone the repo (if you have git) `git clone https://github.com/gr8guyrabi/meetups.git` || download the repo (if you don't have git).
2. Open your terminal and cd (change directory) to the repo root.
3. make sure your `docker` && `docker-compose` are installed correctly. (run `docker --version && docker-compose --version` terminal and make sure no error occurs)
4. make sure your `docker desktop` is running.
5. run command ` docker-compose run web django-admin startproject django_meetups_project . ` '.' in the end is mandatory, 'your_project_name' should not contain spaces and '-'(dash).
6. run command ` docker-compose up `
7. open http://localhost:8000

# Add new app to project
1. make sure your command ` docker-compose up ` is up and running.
2. open up a new terminal and run command ` docker ps `. (Displays a list of docker containers currently running)
3. Find the name of the docker container that you want to add a new app to. (something like `meetups_web_1`)
4. Run command ` docker exec meetups_web_1 python manage.py startapp {app_name}`.

**Note:**
you don't need to navigate to your project folder. But it's recommended not to exec any command outside of the project folder.

# Create database structure using models
1. Create a class representing database structure inside models.py in meetups app.
2. run command `docker exec meetups_web_1 python manage.py makemigrations` to create migration for you models.
3. run command `docker exec meetups_web_1 python manage.py migrate` to migrate above created migration to database structure.

# Admin
1. run command `docker exec meetups_web_1 python manage.py createsuperuser`. if you get an error try `docker exec -it meetups_web_1 python manage.py createsuperuser`
2. follow along to create admin user by adding credentials from terminal.
3. Go to http://localhost:8000/admin

**Note:**
you'll need to create your admin credentials to have access to your admin panel. There's no pre-defined admin credentials.

-----------
**NOTE:**
you need to provide extra options to `docker exec --Options meetups_web_1` 
--Options might include:
`-i` : Keep STDIN open even if not attached
`-it` : Allocate a pseudo-tty. Tells Docker to allocate a virtual terminal session within the container (add this when you need to input your choice from terminal)
For example: `docker exec -it meetups_web_1 ........`

-----------