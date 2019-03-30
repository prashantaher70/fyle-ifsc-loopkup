from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import func
from domain import Bank
from domain import Branch
import os

engine = create_engine(os.environ['DATABASE_URL'], echo=True)

def __session():
    return sessionmaker(bind=engine)()


def banks(limit=1):
    session = __session()
    return session.query(Bank).limit(limit).all()


def branch_by_ifsc(ifsc):
    session = __session()
    return session.query(Branch)\
        .filter(func.lower(Branch.ifsc) == func.lower(ifsc))\
        .first()


def branch(bank_name, city):
    if not (bank_name and city):
        raise AssertionError("provide both city and bank_name")

    session = __session()
    filters = list()

    filters.append(func.lower(Bank.name) == func.lower(bank_name))
    filters.append(func.lower(Branch.city) == func.lower(city))

    q = session.query(Branch, Bank)\
        .join(Bank)

    for f in filters:
        q = q.filter(f)
    bank_branches = q.all()
    branches = []
    for tuple in bank_branches:
        b = tuple[0]
        setattr(b, 'bank', tuple[1].name)
        branches.append(b)
    return branches
