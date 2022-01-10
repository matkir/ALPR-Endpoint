FROM openalpr/openalpr

# Install prerequisites, in apt and npm.
RUN apt-get update\
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3-dev \
    python3-pip \
    wget \
    nano



ADD app.py .
ADD images/car.jpg .
ADD images/empty.jpg .
ADD requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000
#ENTRYPOINT [ "bash" ]
ENTRYPOINT ["waitress-serve","--port=5000", "app:app"]