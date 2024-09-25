#!/bin/bash
sudo yum update -y
sudo yum install -y python3-pip
cd /home/ec2-user/my_app
pip3 install -r requirements.txt
