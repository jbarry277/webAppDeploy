# webAppDeploy

This is the repo for my python flask API, apologies for the misleading repo name

Application.py contains the entire API file 


Endpoints:

https://topapi.azurewebsites.net/addMovie{
  POST: adds the given movie to the database under the given user's id
 }
 https://topapi.azurewebsites.net/home {
  GET (args: userId): returns all of the given users movies
  
  DELETE (args: movie_id) : deletes the given movie
 }
  https://topapi.azurewebsites.net/movieRating{
  POST: updates the given movies rating with the rating given
  }
  
   https://topapi.azurewebsites.net/topTenRanking{
    GET: returns the users top 10 ranked movies, if they exist
    POST: adds or updates a ranking 
   }
  
 
 
