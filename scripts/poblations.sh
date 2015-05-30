#!/bin/bash
workon primeraparte
echo "migrando la bd...."
cd ..
python manage.py shell < cargadebd.py
echo "terminado.. OK!"