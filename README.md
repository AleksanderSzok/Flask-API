# Flask-API

http://aszok-api-1.herokuapp.com/

This is simple API to write down, return saved and edit short texts (up to 160 characters). Each text has it's own id and counter.
It was deployed on heroku platform (instructions at the end of readme file).
It is recommend to install JSON extension to your browser for better text display.

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
  
