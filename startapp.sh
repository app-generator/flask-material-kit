#!/bin/bash
export FLASK_APP=run.py FLASK_ENV=production #development #or #production 
export DB_ENGINE=postgresql
export DB_USERNAME=mlf
export DB_PASSWORD=rainbows
export DB_HOST=192.168.0.179
export DB_PORT='5433'
export DB_NAME=acrp     
#export SQLALCHEMY_DATABASE_URI='postgresql://mlf:rainbows@192.168.0.179:5433/acrp'
export SQLALCHEMY_DATABASE_URI='postgresql://mfoust:EulbogUuAHvQgUs9yG6DDY8BVV6MbeJi@dpg-chqvo0ik728ivvo2uhc0-a.frankfurt-postgres.render.com/acrpresources'
export RENDER_DB_URL='postgresql://mfoust:EulbogUuAHvQgUs9yG6DDY8BVV6MbeJi@dpg-chqvo0ik728ivvo2uhc0-a.frankfurt-postgres.render.com/acrpresources'
export RENDER_DB_HOST='dpg-chqvo0ik728ivvo2uhc0-a.frankfurt-postgres.render.com'
export RENDER_DB_PORT='5432'
export RENDER_DB_NAME=acrpresources
export RENDER_DB_USERNAME=mfoust
export RENDER_DB_PASSWORD=EulbogUuAHvQgUs9yG6DDY8BVV6MbeJi
export YOUR_API_KEY=AIzaSyDDRJijGYKeAfDEUywTOM3AfvHx1Tc_Eho
export YOUR_SEARCH_ENGINE_ID_ACRP='13b46c106c4834523'
flask run #--debugger
