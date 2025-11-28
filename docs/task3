#Command Used

# Build image
docker build -t flask-backend:v1 .

# Run container
docker run -d -p 5000:5000 flask-backend:v1

# Test
curl http://localhost:5000


#OutPut

docker images
REPOSITORY                    TAG        IMAGE ID       CREATED          SIZE
flask-backend                 v1         5540f04c6a22   10 minutes ago   150MB


docker run -d -p 5000:5000 flask-backend:v1
f92fc0c8ab59de07076ce6f39f46b64dc7c7e808b56bd8a87b3d94fd1668cea3
bala@Ubuntu-server:~/bmw-techwork-assignment/backend$ docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED         STATUS         PORTS                                                                                                                                  NAMES
f92fc0c8ab59   flask-backend:v1                      "python app.py"          8 seconds ago   Up 7 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp                b


curl http://localhost:5000

This is flask docker app
