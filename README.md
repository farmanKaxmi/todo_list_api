# Django Redis Celery Task List Project

This is a Django project that uses Redis as a Celery broker for handling asynchronous tasks. It includes basic user authentication with signup and login features, as well as a task list with CRUD functionality.

## Requirements

- Docker
- Docker Compose

## Getting Started

**1. Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project

**1 - Build and start the project using Docker Compose:**

docker-compose up --build -d

**2 - Access the Django development server at http://localhost:8000.**
   Project Structure
      web: Django web application.
      redis: Redis server for Celery.
      celery: Celery worker.

**Features**
    User Authentication:
       Signup: Register new users.
       Login: Authenticate and log in users.
    Task List:
       Create: Add new tasks to the list.
       Read: View the list of tasks.
       Update: Edit and update existing tasks.
       Delete: Remove tasks from the list.
**Usage**
     Visit http://localhost:8000 in your web browser to access the Django web application.
     Use the provided user authentication features for signup and login.
     Explore the task list and perform CRUD operations.

**POSTMAN COLLECTION LINK**
https://api.postman.com/collections/14931068-3e69f18b-04ac-48f2-b164-3cc564a99672?access_key=PMAT-01HRHTRE53DC5NC3W032PYQ7QN

authentication : Bearer token

