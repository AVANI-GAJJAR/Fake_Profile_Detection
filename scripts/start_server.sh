#!/bin/bash
sed -i 's/\[]/\["54.175.190.186"]/' /home/ubuntu/Fake_Profile_Detection/Fake_Profile_Detection/settings.py

python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic
python manage.py runserver 
chmod +x /home/ubuntu/Fake_Profile_Detection/scripts/start_server.sh
