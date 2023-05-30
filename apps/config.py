import os, random, string

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')  
    
    # Set up the App SECRET_KEY
    SECRET_KEY  = os.getenv('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))     

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_ENGINE   = os.getenv('DB_ENGINE'   , default='postgresql')
    DB_USERNAME = os.getenv('RENDER_DB_USERNAME' , default='postgres')
    DB_PASS     = os.getenv('RENDER_DB_PASSWORD' , None)
    DB_HOST     = os.getenv('RENDER_DB_HOST'     , default='localhost')
    DB_PORT     = os.getenv('RENDER_DB_PORT'     , None)
    DB_NAME     = os.getenv('RENDER_DB_NAME'     , None)

    USE_SQLITE  = False

    # try to set up a Relational DBMS
    if DB_ENGINE and DB_NAME and DB_USERNAME:

        try:
            
            # Relational DBMS: PSQL, MySql
            # SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
            #     DB_ENGINE,
            #     DB_USERNAME,
            #     DB_PASS,
            #     DB_HOST,
            #     DB_PORT,
            #     DB_NAME
            # ) 
            SQLALCHEMY_DATABASE_URI = 'postgresql://mfoust:XyjzYX9Acng2dTwg4rIWFUA2Q6Osm2w5@dpg-chqva9fdvk4goev0hcv0-a/acrp_yq3c'

            USE_SQLITE  = False

        except Exception as e:

            print('> Error: DBMS Exception: ' + str(e) )
            print('> Fallback to SQLite ')    

    if USE_SQLITE:

        # This will create a file in <app> FOLDER
        #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
        SQLALCHEMY_DATABASE_URI = os.getenv('RENDER_DB_URL')
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
