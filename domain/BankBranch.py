from domain.Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Branch(Base):
    __tablename__ = 'bank_branches'

    ifsc = Column(String, primary_key=True)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)

    def __repr__(self):
        return "[ifsc: '%s', bank_id: '%s'," \
               " branch: '%s', address: '%s', city: '%s'," \
               " district: '%s', state: '%s']" % (self.ifsc, self.bank_id, self.branch, self.address,
                                                                   self.city, self.district, self.state)