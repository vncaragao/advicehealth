from flask.json import jsonify
from flask.views import MethodView
from app.repositories.BaseResource import BaseResource
from app.models import Owner

class ManagerOwner(MethodView):
    
    def get(self):
        
        result = BaseResource(Owner).getAll()
        return jsonify(result['result']), result['status']
    
    def post(self):
        
        result = BaseResource(Owner).postData({})
        return jsonify(result), result['status']