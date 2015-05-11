#!/bin/bash

./node_modules/bower/bin/bower install
./node_modules/gulp/bin/gulp.js

#Configurar e instalar apache
apt-get install apache2
apt-get install libapache2-mod-wsgi

mv ./000-default.conf /etc/apache2/sites-available/000-default.conf
service apache2 restart

#Generar documentacion
apt-get install epydoc
epydoc SGP authentication flujos proyectos
