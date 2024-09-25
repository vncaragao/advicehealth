from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
from app.models import db
import uuid

class Car(db.Model):

    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(255), nullable=False, default=uuid.uuid4().hex)
    color_id = Column(Integer, ForeignKey('color.id'), nullable=False )    
    model_id = Column(Integer, ForeignKey('model.id'), nullable=False ) 
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False )   
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
