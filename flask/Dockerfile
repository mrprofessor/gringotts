FROM python:3.8

RUN mkdir -p /var/www/flask

# Update working directory
WORKDIR /var/www/flask

# copy everything from this directory to server/flask docker container
COPY . /var/www/flask/

# Give execute permission to below file, so that the script can be executed by docker.
RUN chmod +x /var/www/flask/entrypoint.sh

RUN chmod +rw /var/www/flask/passwords.json

# Install uwsgi
RUN pip3 install uwsgi

# Install the Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

# COPY uswgi.ini
COPY ./uwsgi.ini /etc/uwsgi.ini

# Install the Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

# run server
CMD ["./entrypoint.sh"]
