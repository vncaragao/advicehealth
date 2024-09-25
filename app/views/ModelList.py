from flask.json import jsonify
from flask.views import MethodView
from app.repositories.BaseResource import BaseResource
from app.models.Model import Model

class ModelList(MethodView):
    
    def get(self):
        
        result = BaseResource(Model).getAll()
        return jsonify(result['result']), result['status']