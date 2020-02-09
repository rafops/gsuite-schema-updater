FROM ubuntu:18.04
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN apt-get update
RUN apt-get install -qy \
    python3 \
    python3-pip
RUN python3 -m pip install --upgrade \
    pip \
    google-api-python-client \
    google-auth-httplib2 \
    google-auth-oauthlib
WORKDIR /root/workdir
