from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from domain import Bank
from domain import BankBranch
import os

engine = create_engine(os.environ['DATABASE_URL'], echo=True)


def __session():
    return sessionmaker(bind=engine)()


def banks(limit=1):
    session = __session()
    return session.query(Bank).limit(limit).all()


def branch_by_ifsc(ifsc):
    session = __session()
    return session.query(BankBranch)\
        .filter(func.lower(BankBranch.ifsc) == func.lower(ifsc))\
        .first()


def branch(bank_name, city):
    session = __session()
    filters = list()
    if bank_name:
        filters.append(func.lower(BankBranch.bank_name) == func.lower(bank_name))
    if city:
        filters.append(func.lower(BankBranch.city) == func.lower(city))

    if not bank_name and not city:
        raise AssertionError("provide either city or bank_name or both")

    q = session.query(BankBranch)
    for f in filters:
        q = q.filter(f)
    return q.all()

