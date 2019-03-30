from domain.Base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Bank(Base):
    __tablename__ = 'banks'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "[name: '%s', id: '%s']" % (self.name, self.id)