#!/bin/sh

#Instaladores en gral para el entorno de trabajo

# 1- Virtualenv y virtualenvwrapper
#	-necesitamos pip y para instalar pip necesitamos easy_install
wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
#	-luego pip
sudo easy_install pip
#	-luego agregamos pip al autocompletado del bash
pip completion --bash >> ~/.bashrc
#	-habilitamos con
source ~/.bashrc
#finalmente instalamos virtualenv y virtualenvwrapper
sudo pip install virtualenv
sudo pip install virtualenvwrapper
#2- luego enviamos el WORKON_HOME la direccion de ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs
#se puede ver donde esta por si se necesita
echo "$WORKON_HOME"
#3- luego creamos el WORKON_HOME
mkdir $WORKON_HOME
#4- luego para que pueda saber donde estan los entornos virtuales
echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc
#5- el virtualenvwrapper necesita el paso anterior para ser reconocido
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
#6- Ultimo hacer esto para guardar los cambios y habilitar los comandos
source ~/.bashrc


##Para usar el virtualenv se debe primero crear el entorno:
##mkvirtualenv nombreDelEntornoVirtual
##para desactivar el entorno es:
##deactivate
##para activar algun entorno es:
##workon nombreDeAlgunEntornoCreadoConMKVIRTUALENV
##Para borrar algun entorno es:
##rmvirtualenv nombreEntornoVirtual

###########################
##COMO CREE MI ENTORNO
mkvirtualenv is2
##o si ya lo crearon es equivalente a:
##workon is2
##Seguir con el tutorial http://django-angular.readthedocs.org/en/latest/installation.html
##Instalar djangular pero antes django y angularjs
sudo easy_install django
##necesito el restframework
pip install djangorestframework
##necesito el django restframework jwt (json web token) ya decidimos no usar por falta de documentacion
#pip install djangorestframework-jwt
##para angular necesitamos nodejs
sudo apt-get install nodejs
##luego instalar npm
sudo apt-get install npm
##luego creamos un link simbolico a node
sudo ln -s /usr/bin/nodejs /usr/bin/node
##corroborar las versiones con
node -v
npm -v
##para renombrar todo lo que diga node a nodejs
sudo apt-get install nodejs-legacy npm
##volver a corroborar con
nodejs --version
npm --version

##para descargar dependencias una vez tenga creado el proyecto AngularJS
##cd sgp
##npm install
##eso instalara:	
##    Bower - client-side code package manager
##    Http-Server - simple local static web server
##    Karma - unit test runner
##    Protractor - end to end (E2E) test runner
##Nota: tambien este comando activara a bower para que instale las dependencias de angularjs en app/bower_components

##El proyecto esta preconfigurado con un numero de scripts de ayuda de npm que ayuda a hacer correr facilmente las tareas comunes que necesitaras durante el desarrollo (Probablemente no usado sino cuando miremos logs en angularjs):
##    npm start : start a local development web-server
##    npm test : start the Karma unit test runner
##    npm run protractor : run the Protractor end to end (E2E) tests
##    npm run update-webdriver : install the drivers needed by Protractor

##Nosotros instalaremos manualmente el bower con:
sudo npm install -g bower

##para hacer correr el bower e instalar dependencias de angularjs en la carpeta del proyecto de angular
bower install
#sino funciona probar bower  --allow-root install
#si vuelve a fallar usar sudo
## en la ultima linea se especifica mejor el uso de bower

###########################
##instalar djangular decidimos no usar
#pip install django-angular
###########################

## ojo por favor volver a instalar django 1.7 ya que la version se actualizo automaticamente en pycharm ---> COMPLETADO EL 09/03/2015 00hs
## ahora soporta django 1.9 :)

##instalar django rest framework
pip install djangorestframework

##Instalacion de postgres
sudo apt-get install postgresql postgresql-contrib postgresql-server-dev-all

##Django==1.7 PyJWT==0.2.1 djangorestframework==2.4.3 djangorestframework-jwt==1.0.1 wsgiref==0.1.2
## ya tenemos todo con el django 1.9 sin JWT por la decision anterior
