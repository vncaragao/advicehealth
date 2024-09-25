from app.models import db, Car, Owner

class PedestrianRepository():
    
    def list():
        
        try:
            query = db.session.query(
                Owner.id,                
                Owner.name            
            ).outerjoin(
                Car
            ).filter(
                Car.owner_id.is_(None)
            ).all()
            
            result = []
            for row in query:
                result.append({
                    "id": row[0],
                    "name": row[1]
                })
            
            status = 200 if len(result)> 0 else 404
            
            return {'result': result, 'status': status}
                
        except Exception as e:
            print(e)
            return {'result': {}, 'status': 406}
