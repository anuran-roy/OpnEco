#!/bin/bash

echo "Installing OpnEco..."
echo "Step 1/5: Copying files to /usr/local/OpnEco..."
sudo mkdir /usr/local/OpnEco
sudo cp -R ./OpnEco/ ./OpnEmo/ ./OpnInsights/ ./OpnKeywords/ ./static/ ./templates/ ./manage.py ./db.sqlite3 ./init.py ./requirements.txt ./README.md ./start.sh /usr/local/OpnEco
echo "Step 2/5: Resolving dependencies..."
pip3 install -r /usr/local/OpnEco/requirements.txt
echo "Step 3/5: Initializing for first run..."
python3 /usr/local/OpnEco/init.py
sudo chmod +x /usr/local/OpnEco/start.sh
echo "Step 4/5: Adding OpnEco as a command..."
echo 'alias OpnEco="cd /usr/local/OpnEco; /usr/local/OpnEco/start.sh"' >> ~/.bashrc
echo "Step 5/5: Creating desktop launcher..."
sudo cp OpnEco.desktop ~/Desktop