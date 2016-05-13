#!/bin/bash
workon is2
echo "migrando la bd...."
cd ..
python manage.py shell < cargadebd.py
echo "terminado.. OK!"