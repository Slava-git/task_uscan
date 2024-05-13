

# Note-Taking Application

This project is a note-taking application designed to handle multiple users and their notes. It's built using FastAPI, PostgreSQL and Faiss to provide a robust backend system. 
PostgreSQL can be scaled horizontally in case we need to manage million users.
FastAPI is built to support asynchronous request handling, allowing external service not to block the server process. 
Faiss search is fast in case of handling vast datasets.

## Entities relationship
![Entity Relationship Diagram](https://github.com/Slava-git/task_uscan/blob/master/assets/entities_relationship.png?raw=true)

## Search chart


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
curl -v -X POST "http://localhost:8000/notes/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "content": "Remember to review FastAPI documentation."}'
```
### Search
```bash
curl -v "http://localhost:8000/search/1?query=Do%20you%20have%20an%20appointment%20to%20dentist?" \
     -H "Accept: application/json"
```
