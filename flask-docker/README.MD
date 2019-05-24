# flask-restful package needed to run
pip3 install flask-restful

# docker build
docker build -t flaskapp:latest .

# start container
docker run -it -d -p 5000:5000 flaskapp

# check docker image status
docker ps