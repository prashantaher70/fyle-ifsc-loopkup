from db import dao
from db.serializer import AlchemyEncoder
from functools import wraps

from flask import Flask, request, Response
import json

app = Flask(__name__)


def serialize(func):
    @wraps(func)
    def serializer(*args, **kwargs):
        try:
            return json.dumps(func(*args, **kwargs), cls=AlchemyEncoder)
        except AssertionError as e:
            return Response('{"error" : "%s"} ' % str(e), status=400, mimetype='application/json')
    return serializer


@app.route("/bank/branch/<ifsc>", methods=['GET'])
@serialize
def branch(ifsc):
    branch = dao.branch_by_ifsc(ifsc)
    if branch:
        return branch
    return dict()


@app.route("/bank/branch", methods=['GET'])
@serialize
def branches():
    name = request.args.get('bank_name')
    city = request.args.get('city')
    bank_branches = dao.branch(name, city)
    if bank_branches:
        return bank_branches
    return list()