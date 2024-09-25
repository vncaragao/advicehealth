from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from app.models import db
import uuid

class Owner(db.Model):

    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(255), nullable=False, default=uuid.uuid4().hex)
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }