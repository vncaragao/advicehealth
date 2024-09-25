from app.models import db, Car, Model, Color, Owner

class CarsRepository():
    
    def listCars():
        
        try:
            query = db.session.query(
                Car.id,
                Car.name,
                Owner.name,
                Model.description,
                Color.description
            ).join(
                Model
            ).join(
                Color
            ).join(
                Owner
            ).all()
            
            result = []
            for row in query:
                result.append({
                    "id": row[0],
                    "name": row[1],
                    "owner": row[2],
                    "model": row[3],
                    "color": row[4]
                })
            
            status = 200 if len(result)> 0 else 404
            
            return {'result': result, 'status': status}
                
        except Exception as e:
            print(e)
            return {'result': {}, 'status': 406}
        
    def OwnerCars(owner_id):
        try:
            query = db.session.query(
                Car.id,
                Car.name,
                Model.description,
                Color.description
            ).join(
                Model
            ).join(
                Color
            ).filter(
                Car.owner_id == owner_id
            ).all()
            
            result = []
            for row in query:
                result.append({
                    "id": row[0],
                    "name": row[1],
                    "model": row[2],
                    "color": row[3]
                })
            
            status = 200 if len(result)> 0 else 404
            
            return {'result': result, 'status': status}
                
        except Exception as e:
            print(e)
            return {'result': {}, 'status': 406}