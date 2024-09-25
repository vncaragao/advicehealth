from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from app.models import db

class Color(db.Model):

    __tablename__ = 'color'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    description = Column(String(255), nullable=False)    
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
