from app.models import db
from sqlalchemy import desc

class BaseResource:

    def __init__(self, model):
        self.model = model

    def getAll(self, params={}):
        try:            
            query = self.model.query.filter_by(**params).all()            
            result = [r.serialize for r in query]            
            if len(result) > 0:
                return {'result': result, 'status':200}
            return {'result': result, 'status':404}
            
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}
    
    def getFirst(self, params={}):
        try:
            query = self.model.query.filter_by(**params).first()
            status = 200
            if query == None:
                query = []
                status = 404
            else:
                query = [query.serialize]
            return {'result': query[0], 'status':status}
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}
    
    def getAllExcept(self, params={}):
        try:
            query = self.model.query.filter(
                self.model.company_id == params['company_id'],
                self.model.id != params['id']
                ).all()

            result = [r.serialize for r in query]

            if len(result) > 0:
                return {'result': result, 'status':200}
            return {'result': [], 'status':200}
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}   
    
    def getLastData(self, params={}):
        try:
            query = self.model.query.filter_by(**params).order_by(desc(self.model.id)).first()
            status = 200
            if query == None:
                query = []
                status = 404
            else:
                query = [query.serialize]
            return {'result': query[0], 'status':status}
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}
    
    def getAllOrderByDesc(self, params={}, column=""):
        try:            
            query = self.model.query.filter_by(**params).order_by(desc(column)).all()          
            result = [r.serialize for r in query]
            #print(dir(self.model.query))
            if len(result) > 0:
                return {'result': result, 'status':200}
            return {'result': result, 'status':404}
            
        except Exception as error:
            return {'result':[], 'msg': str(error), 'status':404}
    
    def postData(self, data):
        try:
            query = self.model(**data)
            db.session.add(query)
            db.session.commit()
            
            return {'msg': 'Criado com sucesso', 'status': 201}
        except Exception as error:
            db.session.rollback()
            return {'msg': str(error), 'status':406}
        finally:
              db.session.close()
              
    def putData(self, params, data):
        try:
            self.model.query.filter_by(**params).update({k: v for k, v in data.items()})
            db.session.commit()
                        
            return {'msg': 'Atualizado com sucesso', 'status': 200}
        except Exception as error:
            db.session.rollback()
            return {'msg': str(error), 'status':406}
        finally:
              db.session.close()