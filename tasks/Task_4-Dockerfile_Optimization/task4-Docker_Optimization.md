#Command Used

# Build image
docker build -t flask-backend:optimized -f Dockerfile.optimized .
docker images

#Output

docker images | grep flask*
flask-backend                 optimized   f0416e9d60fd   12 minutes ago   126MB
flask-backend                 v1          6cf3d26c06f2   20 hours ago     150MB

#Method
Multistage docker build.

This multi-stage Dockerfile installs dependencies in a temporary build layer and only copies necessary runtime files into the final image. This results in reduced image size.

#Build stage

1) 1st stage build, were all dependies and install in the build stage.
2) PYTHONDONTWRITEBYTECODE=1 --> disable .pyc files (no unnecessary bytecode)
   PYTHONUNBUFFERED=1 --> better container logging (no output buffering)
3) installed the python dependcies in seperate folder name as install with no cache in the image.

#Runtime stage

1) COPY --from=builder /install /usr/local --> this copy on the installed depedencies
2) COPY app.py . --> Only copies the application code. which ignore virtual enviroment and junks.



