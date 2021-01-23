echo 'Starting external server'
SHELL_PATH=`pwd -P`

source /home/pi/refillable-backend/env/bin/activate
python /home/pi/refillable-backend/src/manage.py runserver 0.0.0.0:8001