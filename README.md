# docker-flask-app
Example Dockerized "Hello World" Flask App

## Running Locally

```bash
docker run --rm -p 8080:8080 -it $(docker build -q .)
```
then visit http://localhost:8080
