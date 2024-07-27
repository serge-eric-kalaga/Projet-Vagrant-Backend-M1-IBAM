@ echo off
cd db
echo *******************Demarrage du serveur de base de donnée**********************
vagrant up

cd ..

cd web
echo *******************Demarrage du serveur web**********************
vagrant up

cd ..

cd app
echo *******************Demarrage du serveur d'application**********************
vagrant up