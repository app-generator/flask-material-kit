#!/bin/bash
export FLASK_APP=run.py FLASK_ENV=production #development #or #production 
export DB_ENGINE=postgresql
export DB_USERNAME=mlf
export DB_PASSWORD=rainbows
export DB_HOST=192.168.0.179
export DB_PORT='5433'
export DB_NAME=acrp     
#export SQLALCHEMY_DATABASE_URI='postgresql://mlf:rainbows@192.168.0.179:5433/acrp'
export RENDER_DB_URL='postgres://mfoust:zChN3MF18PFWdAoN4vmrclQSZWljgvZh@dpg-chn16v67avj3o34jnabg-a.ohio-postgres.render.com/acrp'
export RENDER_DB_HOST='dpg-chn16v67avj3o34jnabg-a.ohio-postgres.render.com'
export RENDER_DB_PORT='5432'
export RENDER_DB_NAME=acrp
export RENDER_DB_USER=mfoust
export RENDER_DB_PW=zChN3MF18PFWdAoN4vmrclQSZWljgvZh
export YOUR_API_KEY=AIzaSyDDRJijGYKeAfDEUywTOM3AfvHx1Tc_Eho
export YOUR_SEARCH_ENGINE_ID_ACRP='13b46c106c4834523'
flask run #--debugger
