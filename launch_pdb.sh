

CONTAINER_ID=$(sudo docker ps --filter "name=todo_web_1" -q)

sudo docker container attach $CONTAINER_ID

