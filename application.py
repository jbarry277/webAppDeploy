import pyodbc
from flask import Flask, request,jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
import mysql.connector
from SQLhelpers import *
##from endpoints.addMovie import Hello
import pyodbc
server = 'topserver1.database.windows.net'
database = 'topDatabase'
username = 'topAdmin'
password = 'Mitsilancer1'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
app = Flask('topAPI')
CORS(app)


@app.route('/addMovie',methods = ['GET', 'POST'])

def addMovie():
    if(request.method == 'POST'):
        data = request.get_json()

        movieName = data['movieName']
        movieYear = data['year']
        user_id = data['userId']
        rating = 0
        posterURL = data['posterURL']
        statement = 'INSERT INTO movies (movieName,movieYear,posterURL,user_id,rating) VALUES (?,?,?,?,?)'
        cursor.execute(statement,movieName,movieYear,posterURL,user_id,rating)
        conn.commit()
        return jsonify('done')

    if(request.method == 'GET'):

        return 'he'

@app.route('/home', methods = ['GET','DELETE'])
def getMyMovies():
    ## this returns all of the movies for a given user
    if(request.method == 'GET'):
        ## data is sent via url paramaters
        data = request.args
        user_id = data['userId']
        statement = 'SELECT * FROM movies WHERE user_id = '+user_id

        cursor.execute(statement)
        movies = cursor.fetchall()
        returnData = []

        for row in movies:
            returnData.append(list(row))

        return jsonify(returnData)
        return 'no movies'

    ## this deletes a given movie
    if(request.method == 'DELETE'):
        data = request.get_json()

        deleteMovie_id = (data['movieId'])

        statement = "DELETE FROM movies WHERE movie_id = "+str(deleteMovie_id)
        cursor.execute(statement)
        conn.commit()
        return jsonify(data)

@app.route('/movieRating',methods = ['POST','GET'])
def updateRating():
    if(request.method == 'POST'):
        data = request.get_json()

        movie_id = str(data['movie_id'])
        rating = str(data['rating'])

        statement = "UPDATE movies SET rating = ? WHERE movie_id= ?"
        cursor.execute(statement,rating,movie_id)
        conn.commit()
        return 'rating updated'


@app.route('/topTenRanking',methods = ['POST','GET'])
def topTenRanking():
    if(request.method == 'GET'):
        ## returns the users top 10 ranking
        ## data is sent via url paramaters
        data = request.args
        user_id = data['userId']

        statement = "SELECT * FROM topTen WHERE user_id = "+user_id
        cursor.execute(statement)
        rankedMovies = cursor.fetchall()
        returnData = []
        for row in rankedMovies:
            returnData.append(list(row))

        return jsonify(returnData)
    if(request.method =='POST'):

        data = request.get_json()
        movie_id = str(data['movieId'])
        user_id = str(data['userId'])
        movieName = str(data['movieName'])
        posterURL = str(data['posterURL'])
        ranking = str(data['ranking'])
        ## checking that no movie exists already at that rank
        rankingExists = True
        checkStatement = "SELECT * FROM topTen WHERE user_id ="+user_id+'AND ranking='+ranking
        cursor.execute(checkStatement)
        checkRankings = cursor.fetchall()
        if(len(checkRankings) == 0):
            rankingExists = False

        if(rankingExists == False):
            statement = "INSERT into topTen (movieName,posterURL,user_id,ranking,movie_id) VALUES (?,?,?,?,?)"
            cursor.execute(statement,movieName,posterURL,user_id,ranking,movie_id)
            conn.commit()
            return 'ranking inserted'


        if(rankingExists):
            statement = "UPDATE topTen SET movieName = ?,posterURL = ?, movie_id = ? WHERE ranking = ?"
            cursor.execute(statement,movieName,posterURL,movie_id,ranking)

            conn.commit()
            return 'ranking updated'

if __name__ == '__main__':
   app.run(port='5002')
