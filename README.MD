# Note-Taking Application

This project is a note-taking application designed to handle multiple users and their notes. It's built using FastAPI and PostgreSQL to provide a robust backend system. The application is suitable for personal note management and is scalable to support multiple users with secure access and storage.

## Features

- **User Management**: Supports creating users and managing user sessions.
- **Note Management**: Allows users to create, retrieve, update, and delete notes.
- **Search Functionality**: Users can search for notes based on content.

## Requirements

- Python 3.10
- Docker and Docker Compose

## Local Development Setup

To set up and run the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/note-taking-app.git
cd note-taking-app
```
### 2. Build and Run with Docker

```bash
docker-compose up --build
```

## Api usage
Here are a few examples of how you can interact with the API using curl:
### Create a User
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "john", "email": "john@example.com"}' http://localhost:8000/users/
```

### Add a Note
```bash
curl -X POST -H "Content-Type: application/json" -d '{"content": "Remember the milk"}' http://localhost:8000/notes/?user_id=1
```
### Search
```bash
curl "http://localhost:8000/search/{user_id}?query=Do you have an appointment to dentist?"
```