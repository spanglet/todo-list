
# Main Dockerfile for flax project

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
EXPOSE 5000
WORKDIR /app

COPY ./wait-for-it.sh ./wait-for-it.sh
RUN chmod +x wait-for-it.sh

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

ENTRYPOINT ["/bin/bash"]
CMD ["./wait-for-it.sh","-h","mysqldb","-p","3306","--","python3","-m", "flask","run","--host=0.0.0.0"]

