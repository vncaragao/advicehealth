from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.repositories.BaseResource import BaseResource
from app.repositories.CarsRepository import CarsRepository
from app.models import Car, Color, Model, Owner


class ManagerCar(MethodView):
    
    def get(self):
        
        result = CarsRepository.listCars()
        return jsonify(result['result']), result['status']
    
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('color_id', required=True)
        parse.add_argument('model_id', required=True)
        parse.add_argument('owner_id', required=True)
        data = parse.parse_args()  
        
        verifyColor = BaseResource(Color).getFirst({"id": data['color_id']})
        if verifyColor['status'] != 200:
            return jsonify({"msg": "Essa cor não existe."}), 401
        
        verifyModel = BaseResource(Model).getFirst({"id": data['model_id']})
        if verifyModel['status'] != 200:
            return jsonify({"msg": "Esse modelo não existe."}), 401
        
        verifyOwner = BaseResource(Owner).getFirst({"id": data['owner_id']})
        if verifyOwner['status'] != 200:
            return jsonify({"msg": "Esse proprietário não existe."}), 401
        
        verifyQttCarOwner = BaseResource(Car).getAll({"owner_id": data['owner_id']})
        if len(verifyQttCarOwner['result']) >= 3:
            return jsonify({"msg": "Esse proprietário está com a quantidade máxima de carros."}), 401
        
        result = BaseResource(Car).postData(data)
        return jsonify(result), result['status']