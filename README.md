# Docker
Please run this command to create the image from the Dockerfile

- sudo docker build -t <repository/app-name:tag> .

Then run the container using this command

- docker run -it -v $PWD:/opt <repository/app-name:tag>
