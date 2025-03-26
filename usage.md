#!/bin/bash

echo "🔹 Instalando dependencias necesarias..."
sudo apt update && sudo apt install -y docker.io docker-compose python3 python3-pip mosquitto mosquitto-clients

echo "🔹 Instalando Zeek IDS..."
sudo apt install -y zeek
sudo systemctl enable zeek
sudo systemctl start zeek

echo "🔹 Instalando Node-RED..."
sudo npm install -g --unsafe-perm node-red

echo "🔹 Instalando librerías de Machine Learning..."
pip3 install -r requirements.txt

echo "✅ Instalación completa. Usa 'docker-compose up -d' para iniciar los servicios."
