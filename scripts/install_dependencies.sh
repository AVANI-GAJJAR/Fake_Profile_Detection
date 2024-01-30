#!/bin/bash
sudo apt install -y python3-pip
virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/Fake_Profile_Detection/requirements.txt
chmod +x /home/ubuntu/Fake_Profile_Detection/scripts/install_dependencies.sh
