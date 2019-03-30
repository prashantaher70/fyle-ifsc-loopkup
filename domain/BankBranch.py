from domain.Base import Base
from sqlalchemy import Column, Integer, String


class BankBranch(Base):
    __tablename__ = 'bank_branches'

    ifsc = Column(String, primary_key=True)
    bank_id = Column(Integer)
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    bank_name = Column(String)

    def __repr__(self):
        return "[ifsc: '%s', bank_id: '%s'," \
               " branch: '%s', address: '%s', city: '%s'," \
               " district: '%s', state: '%s', bank_name: '%s']" % (self.ifsc, self.bank_id, self.branch, self.address,
                                                                   self.city, self.district, self.state, self.bank_name)