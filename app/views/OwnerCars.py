from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.repositories.CarsRepository import CarsRepository

class OwnerCars(MethodView):
    
    def get(self):        
        parse = reqparse.RequestParser()               
        parse.add_argument('owner_id', required=True)
        data = parse.parse_args()  
        
        result = CarsRepository.OwnerCars(data['owner_id'])
        return jsonify(result['result']), result['status']