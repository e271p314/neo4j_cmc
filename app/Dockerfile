FROM fedora:latest
RUN dnf -y update && dnf -y install python3 python3-pip && dnf clean all
WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install --user -r requirements.txt
WORKDIR /app
COPY . .
