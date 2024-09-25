import importlib
import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.models import db
from app.entities.CustomJSONEncoder import CustomJSONEncoder

def create_app():
    app = Flask(__name__)    

    app.json_encoder = CustomJSONEncoder    
    
    environ = {        
        'prod': 'app.entities.Config.ProductionConfig'
    }    

    conf = environ.get(os.environ.get('FLASK_CONF', default='prod'))
    app.config.from_object(conf)
    db.init_app(app)
    
    CORS(app)
    Migrate(app=app, db=db, compare_type=True)     

    mod = importlib.import_module('.'.join(conf.split('.')[:-1]))    
    
    try:
        package = importlib.import_module('app.views')
        app.register_blueprint(
            getattr(package, "routes"), url_prefix='/api')
    except Exception as e:
        print(str(e))
        
    return app

app = create_app()

    