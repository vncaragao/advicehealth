from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.repositories.BaseResource import BaseResource
from app.models import Car, Owner

class ManagerTransfer(MethodView):
    
    def put(self):
        parse = reqparse.RequestParser()
        parse.add_argument('car_id', required=True)        
        parse.add_argument('owner_id', required=True)
        data = parse.parse_args()  
        
        verifyCar = BaseResource(Car).getFirst({"id": data['car_id']})
        if verifyCar['status'] != 200:
            return jsonify({"msg": "Esse carro não existe."}), 401
        
        verifyOwner = BaseResource(Owner).getFirst({"id": data['owner_id']})
        if verifyOwner['status'] != 200:
            return jsonify({"msg": "Esse proprietário não existe."}), 401
        
        verifyQttCarOwner = BaseResource(Car).getAll({"owner_id": data['owner_id']})
        if len(verifyQttCarOwner['result']) >= 3:
            return jsonify({"msg": "Esse proprietário está com a quantidade máxima de carros."}), 401
        
        result = BaseResource(Car).putData({"id": data['car_id']}, {"owner_id": data['owner_id']})
        return jsonify(result), result['status']