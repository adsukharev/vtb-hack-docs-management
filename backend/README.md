# RESTful API VTB

#### Note
All data should be sent to server inJSON file.

Schemas are in backend/db/models.py

## Endpoints

 
 ### Sign In
```
POST     /api/signin
```
Example for POST:
```
{
    "login": "test1",
    "password": "123Wertyq"
}
 ```
 
Request:
 ```
{
    "login": "TestUser",
    "id": 1
}
 ```

 ### Log out
```
DELETE     /api/logout
```

### Users

```
GET     /api/users -> get all users
GET     /api/users/<user_id> -> get one user by id
```

Response for getting one user:
```
{
    "user_id": 4,
    "login": "test",
    "email": "test@gmail.com",
   
}

```
### Docs
```
GET     /api/docs  -> get all docs
GET     /api/docs/<doc_id>  -> get doc by id
POST    /api/docs -> start a doc
```
Example POST request
```
{
	"doc_id": 1
}
```

Response GET:
```
{
    "votes": [
        {
            "vote_id": 2,
            "vote_text": "Дальнее зарубежье: В связи с тем, что наш проект заинтересовал транснациональной компанию schneider electric в рамках конкурса Go Green in the City, мы планируем через ее дочерние компании внедрить наше решение в страны Европы и Северной Америки, где основными потребителями с наибольшим объемом рынка и количеством повреждений",
            "plus": 0,
            "minus": 0,
            "doc_id": 1
        },
     ],
     "chats": [
        {
            "chat_id": 1,
            "chat_name": "Опрос 1",
            "vote_id": 1,
            "doc_id": 1,
            "messages": [
                {
                    "creation_date": "today",
                    "text": "asdasd",
                    "author": "Andrei"
                },
                {
                    "creation_date": "today",
                    "text": "asdasd",
                    "author": "Andrei"
                }
            ]
        }
     ],
     "time": 400.2994599342346
}

```
### Votes
```
POST     /api/votes
```
Example POST request
```
{
	"vote_id": 1,
	"user_id": 2,
	"vote": -1 -> -1 vote against, 1 vote for
}
```

### Chats

```
GET     /api/chats  -> get chats of the doc
GET    /api/chats/<chat_id>  -> get the certain chat with messages
```
Example GET response
```
[
    {
        "chat_name": "kek",
        "chat_id": 3
    },
    {
        "chat_name": "cheburek",
        "chat_id": 5
    }
]
```

Example GET <chat_id>  response
```
{
    "messages": [
        {
            "creation_date": "2019-08-07 15:34:07",
            "text": "asdad",
            "author": "test1"
        },
        {
            "creation_date": "2019-08-07 15:34:11",
            "text": "asdd",
            "author": "test2"
        }
    ],
    "partner_id": 2
}
```

### Socket

```
/api/socket -> connect to socket
    
```
Events

on:

```
'connect' -> connected to socket
'receive_message(message)' -> get message from server to another user
'notification(message)' -> notificate about message, fake, history, likes, dislikes

```

emit:

```
'connect_logged_user(user_id)' -> after sign in send user_id
```

```
'join(chat_id)' -> send chat_id to join the chat
```

```
'message(message)' -> send message 
{
    "text": "Hello",
    "chat_id": "1", -> get this from url
    "author": "YoYo", -> login of user
    "creation_date": "2019-09-02T09:25:07.561Z", -> new Date(),
    "partner_id": '2'
}
```

```
'manage_notification(data)' -> send notification 
{
    "author": "YoYo", -> login of user
    "partner_id": "2", for whom notification
    "type": "history" or "like" or "dislike" or "fake"
}
```


