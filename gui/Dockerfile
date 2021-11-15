FROM node:lts as dependencies

RUN mkdir -p /var/www/gui

# Update working directory
WORKDIR /var/www/gui

# copy everything from this directory to server/flask docker container
COPY . /var/www/gui/

# Install uwsgi
RUN npm install serve -g

EXPOSE 3000

# run server
CMD serve
