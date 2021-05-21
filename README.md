# Flask-API

http://aszok-api-1.herokuapp.com/

This is simple API to write down, return saved and edit short texts (up to 160 characters). Each text has it's own id and counter.
It was deployed on heroku platform (instructions at the end of readme file).
It is recommend to install JSON extension to your browser for better text display.
Texts are stored in database:

Id | Text      | Counter |
-- |---------- | ------- |
1  | example 1 |    0    |
2  | example 2 |    0    |

## Methods
### GET method

To view all texts just simply paste http://aszok-api-1.herokuapp.com/ in browser.

We can also use cURL command:
```
curl http://aszok-api-1.herokuapp.com/
```
This will give the following output:
```
[{"counter":0,"id":1,"text":"example change message 1"},{"counter":0,"id":11,"text":"example message 3"}]
```
Viewing all texts don't increase counters.

To view particular text, for ex. with id=1, paste http://aszok-api-1.herokuapp.com/text/1 (BASE URL + /text/<id>) or:

```
curl http://aszok-api-1.herokuapp.com/text/1
```
```
{"counter":1,"id":1,"text":"example change message 1"}
```
GET method increase text counter each time by one.

All methods below need authentication. This API uses BasicAuth with username and password. 
### POST method 
We pass new text in form-data, for ex. with cURL:
```
curl -X POST -F "text"="new example text" -u aleksander:szok http://aszok-api-1.herokuapp.com/text --header "Content-Type:multipart/form-data"
```
```
{"counter":0,"id":12,"text":"new example text"}
```
Or with Postman:
![alt text](https://github.com/AleksanderSzok/Flask-API/blob/main/images/postman_post.PNG)
  
Remember to set authorization:
![alt text](https://github.com/AleksanderSzok/Flask-API/blob/main/images/postman_post_auth.PNG)
  
Or with Python requests:
![alt text](https://github.com/AleksanderSzok/Flask-API/blob/main/images/python_post.PNG)
  
### PUT method
  
To change existing text we need to specify id of out text, for example for id=14:
```
curl -X PUT -F "text"="new changed text 14" -u aleksander:szok http://aszok-api-1.herokuapp.com/text/14 --header "Content-Type:multipart/form-data"
```
```
{"counter":0,"id":14,"text":"new changed text 14"}
```
Or Postman:
![alt text](https://github.com/AleksanderSzok/Flask-API/blob/main/images/postman_put.PNG)
Now we see changes: http://aszok-api-1.herokuapp.com/text/14
  
PUT reset text counter. Sending message with 0 character don't change existing text.
  
### DELETE method

Delete text with cURL (BASE URL + /text/<id>):
```
curl -X DELETE -u aleksander:szok http://aszok-api-1.herokuapp.com/text/13
```
We deleted text with id=13. In Postman:
![alt text](https://github.com/AleksanderSzok/Flask-API/blob/main/images/postman_delete.PNG)
  
## Deploying app on Heroku

This app uses Flask and SQLAlchemy libraries, and is connected to Heroku Postgres database. To achieve that we need to do following steps:
1. Login to heroku and create new app.
2. Activate new python virtual environment, for ex. in PyCharm.
3. cd to main folder and use terminal to pip install all required libraries and psycopg2.
```
pip install flask
pip install flask-sqlalchemy
pip install flask-marshmallow
pip install marshmallow-sqlalchemy
pip install flask-basicauth
pip install psycopg2
```
4. Create requirements.txt file and Procfile:
```
pip freeze > requirements.txt
echo web: gunicorn flaskapi:app > Procfile
```
5. Login to Heroku from PyCharm terminal and create database on Heroku:
```
heroku login
heroku addons:create heroku-postgresql:hobby-dev --app aszok-api-1
```
6. Get database url and paste in flaskapi.py after app.config['SQLALCHEMY_DATABASE_URI'] =:
```
heroku config --app aszok-api-1  
```  
7. Change in database url 'postgres' to 'postgresql'.
8. Follow steps on heroku page:
```
git add .
git commit -m "start"
heroku git:remote -a aszok-api-1
git push heroku master
```
9. Last step is to create all tables in database. From Pycharm terminal run heroku python terminal:
```
heroku run python
>> from flaskapi import db
>> db.create_all()
>> exit()
```
