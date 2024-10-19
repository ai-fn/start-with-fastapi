# Start with FastAPI

### Learning python project using FastAPI framework

1. `Clone Repo`
    ```bash
    git clone https://github.com/ai-fn/start-with-fastapi.git
    ```
2. `Setup environment varialbles`
   #### Now you need to create .env file end setup all of this variables
   | Variable          | Description                            |
   | ----------------- | -------------------------------------- |
   | DB_HOST           | DB host name                           |
   | POSTGRES_USER     | Name of db user                        |
   | POSTGRES_DB       | DB name                                |
   | POSTGRES_PASSWORD | Password for your db user              |
   | FASTAPI_PORT      | Port on which the application will run |

3. `Start Docker Compose Project`
    ```bash
    docker compose up --build -d
    ```
