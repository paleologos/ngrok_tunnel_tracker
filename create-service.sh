#!/bin/bash
touch tunneltracker.service
echo "[Unit]" > tunneltracker.service
echo "Description=Tunnel Tracker" >>tunneltracker.service
echo "After=network.target" >> tunneltracker.service
echo "StartLimitIntervalSec=0" >> tunneltracker.service
echo "[Service]">> tunneltracker.service
echo "Type=simple" >>tunneltracker.service
echo "Restart=always" >>tunneltracker.service
echo "RestartSec=1" >> tunneltracker.service
echo "User=$USER" >> tunneltracker.service
servicedir=`pwd`
echo "WorkingDirectory=$servicedir" >> tunneltracker.service
applocation=`readlink -f app_tracker.py`
echo "ExecStart=python3 $applocation" >>tunneltracker.service
echo "" >>tunneltracker.service
echo "[Install]" >> tunneltracker.service 
echo "WantedBy=multi-user.target" >> tunneltracker.service

# copy to service directory
sudo cp ./tunneltracker.service /etc/systemd/system

# reload daemon 
sudo systemctl daemon-reload

# service status
sudo systemctl status tunneltracker.service

# enable service on reboot
sudo systemctl enable tunneltracker.service

# service start
sudo systemctl start tunneltracker.service

# reload daemon 
sudo systemctl daemon-reload

# service restart
sudo systemctl restart tunneltracker.service

# service status
sudo systemctl status tunneltracker.service