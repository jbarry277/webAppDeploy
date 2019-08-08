import pyodbc
from flask import Flask, request,jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
import mysql.connector
from SQLhelpers import *
##from endpoints.addMovie import Hello
conn = mysql.connector.connect(host='127.0.0.1',
                                           database='topDB',
                                           user='root',
                                           password='')

cursor = conn.cursor()
app = Flask('topAPI')
CORS(app)


@app.route('/home',methods = ['GET', 'POST'])

def movies():
    if(request.method == 'POST'):
        data = request.get_json()
        movieName = data['movieName']
        year = data['year']
        director = data['director']
        cursor.execute('INSERT INTO movies (movieName,director,year) VALUES (%s,%s,%s)',(movieName,director,year))
        conn.commit()
        return jsonify('done')
    if(request.method == 'GET'):
        return 'hi'
if __name__ == '__main__':
   app.run(port='5002')
