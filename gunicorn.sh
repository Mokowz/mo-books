#!/usr/bin/env bash

# Create systemd socket
sudo vi /etc/systemd/system/gunicorn.socket

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

sudo vi /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/sammy/myprojectdir
ExecStart=/home/sammy/mo-books/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          app.wsgi:application

[Install]
WantedBy=multi-user.target

# Start and Enable gunicorn
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo systemctl status gunicorn.socket