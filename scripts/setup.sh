#!/bin/bash
#Configurar e instalar apache
apt-get install apache2
apt-get install libapache2-mod-wsgi

mv ./000-default.conf /etc/apache2/sites-available/000-default.conf
service apache2 restart
