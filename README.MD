# Note-Taking Application

This project is a note-taking application designed to handle multiple users and their notes. It's built using FastAPI, PostgreSQL and Faiss to provide a robust backend system. 
PostgreSQL can be scaled horizontally in case we need to manage million users.
FastAPI is built to support asynchronous request handling, allowing external service not to block the server process. 
Faiss search is fast in case of handling vast datasets.

## Features

- **User Management**: Supports creating users.
- **Note Management**: Allows users to create, retrieve.
- **Search Functionality**: Users can search for notes based on content and ask questions.

## Requirements

- Python 3.10
- Docker and Docker Compose
- OpenAi api key which you need to add in `.env`

## Local Development Setup

To set up and run the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Slava-git/task_uscan.git
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
