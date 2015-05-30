#!/bin/bash

./node_modules/bower/bin/bower install
./node_modules/gulp/bin/gulp.js

#Generar documentacion
apt-get install epydoc
epydoc SGP authentication flujos proyectos sprints userstories
