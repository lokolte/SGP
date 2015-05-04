#!/bin/bash
workon primeraparte
echo "migrando la bd...."
python manage.py shell < cargadebd.py
echo "terminado.. OK!"