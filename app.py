from flask import Flask, request, jsonify
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import create_engine, and_, Text, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql.json import json, JSONB
import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload',methods=['POST'])
def upload():

#    if request.headers['Content-Type'] == 'application/json':
# TO-DO verify json content
#    else:
#        return "415 Unsupported Media Type ;)"


    connection_string = 'postgresql://postgres:postgres@127.0.0.1:5432/postgres'

    db = sqlalchemy.create_engine(connection_string)
    engine = db.connect()

    j_table = sqlalchemy.table(
        "modeldetails",
        Column('id', Text, primary_key=True, autoincrement=True),
        Column('modeldetails', JSONB))

    statement = j_table.insert().values(
        modeldetails=request.json
    )
    engine.execute(statement)

    return "JSON Message OK!"


if __name__ == '__main__':
    app.run(debug=True)
