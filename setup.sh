docker build -t docker-notif .
docker run -d --restart=always --name docker-notif --network=host -v /var/run/docker.sock:/var/run/docker.sock docker-notif