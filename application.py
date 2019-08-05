import pyodbc
import json

from flask import Flask, request
from flask_restful import Resource, Api

import mysql.connector

app = Flask('topAPI')
api = Api(app)




server = 'topserver1.database.windows.net'
database = 'topDB'
username = 'topAdmin'
password = 'Mitsilancer1'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

app.config["DEBUG"] = True


class Home(Resource):
    def put(self):
        createStatement = "INSERT INTO movies (id,movieName) VALUES (1,'hhThe_social_network')"
        cursor.execute(createStatement)
        cursor.commit()
        return 'done'

api.add_resource(Home, '/home') # Route_1

#if __name__ == '__main__':
#     app.run(port='5002')
