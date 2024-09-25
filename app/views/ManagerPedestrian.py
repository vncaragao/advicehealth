from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.repositories.PedestrianRepository import PedestrianRepository

class ManagerPedestrian(MethodView):
    
    def get(self):
        
        result = PedestrianRepository.list()
        return jsonify(result['result']), result['status']