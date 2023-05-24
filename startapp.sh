#!/bin/bash
export FLASK_APP=run.py FLASK_ENV=production #development #or #production 
export DB_ENGINE=postgresql
export DB_USERNAME=mlf
export DB_PASSWORD=rainbows
export DB_HOST=192.168.0.179
export DB_PORT='5433'
export DB_NAME=acrp     
#export SQLALCHEMY_DATABASE_URI='postgresql://mlf:rainbows@192.168.0.179:5433/acrp'
export YOUR_API_KEY=AIzaSyDDRJijGYKeAfDEUywTOM3AfvHx1Tc_Eho
export YOUR_SEARCH_ENGINE_ID_ACRP='13b46c106c4834523'
flask run #--debugger
