from flask.json import jsonify
from flask.views import MethodView
from app.repositories.BaseResource import BaseResource
from app.models.Color import Color

class ColorList(MethodView):
    
    def get(self):
        
        result = BaseResource(Color).getAll()
        return jsonify(result['result']), result['status']