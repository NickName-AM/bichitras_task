# Bichitras Team Task

## Setup
```
$ git clone https://github.com/NickName-AM/bichitras_task.git
$ cd bichitras_task/
$ pip install requirements.txt
```

## Migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Run server
```
$ python manage.py runserver
```


## Request/Response
**Note: Assume that Header: `Authorization: Bearer ACCESS_TOKEN` is given for the required routes.**

1. /api/users/signup/

Request
```
{
    "password": "Test@123",
    "full_name": "Abik Maharjan",
    "email": "maharjanabik061@gmail.com"
}
```
Response
```
{
    "id": 1,
    "last_login": null,
    "full_name": "Abik Maharjan",
    "email": "maharjanabik061@gmail.com",
    "is_active": true
}
```

2. GET /api/profile/ (Header as `Authorization: Bearer ACCESS_TOKEN`)

Response
```
{
    "id": 1,
    "full_name": "Abik Maharjan",
    "email": "maharjanebik061@gmail.com"
}
```

3. /api/users/token/

Request
```
{
    "email": "maharjanabik061@gmail.com",
    "password": "Test@123"
}
```

Reponse
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTg2NDEzOSwiaWF0IjoxNzQ1Nzc3NzM5LCJqdGkiOiJjNTI5YTRiZTE1NTg0NTk2YTE3Y2NkMjcxZTNlY2ZlYSIsInVzZXJfaWQiOjJ9.kDe5xGVbhsxb01QWCQ_pqweoI0z8ZI8sg7XXalQCUFs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1Nzc4MzM5LCJpYXQiOjE3NDU3Nzc3MzksImp0aSI6IjM2NTlmZTIzMTc1YTQwYjM5YmQ4MTY3Y2I0NTdjZGRmIiwidXNlcl9pZCI6Mn0.cCSGaWpvxE69MDOF4c5U5z6_bImqqW0ABmILjcs4xgo"
}
```

4. /api/users/token/refresh/

Request
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTg2NDEzOSwiaWF0IjoxNzQ1Nzc3NzM5LCJqdGkiOiJjNTI5YTRiZTE1NTg0NTk2YTE3Y2NkMjcxZTNlY2ZlYSIsInVzZXJfaWQiOjJ9.kDe5xGVbhsxb01QWCQ_pqweoI0z8ZI8sg7XXalQCUFs"
}
```
Response
```
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1Nzc4NDUyLCJpYXQiOjE3NDU3Nzc3MzksImp0aSI6IjI4YmIwM2YwZWY5MzRhMDhiM2M0MjFjOGVhNzQ0YjRkIiwidXNlcl9pZCI6Mn0.fbJN7Ppc1rZFqlUTXvssEJ0puG4n2_6HxaOJ8mJSiBk"
}
```

5. /api/users/token/blacklist/

Request
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTg2NDEzOSwiaWF0IjoxNzQ1Nzc3NzM5LCJqdGkiOiJjNTI5YTRiZTE1NTg0NTk2YTE3Y2NkMjcxZTNlY2ZlYSIsInVzZXJfaWQiOjJ9.kDe5xGVbhsxb01QWCQ_pqweoI0z8ZI8sg7XXalQCUFs"
}
```

Reponse
```
{}
```

6. GET /api/tasks/

Response
```
[
    {
        "id": 2,
        "title": "Task2",
        "description": "Finish Task App for Bichitras",
        "status": "CD"
    },
    {
        "id": 3,
        "title": "Task3",
        "description": "Finish Task App for Bichitras Task3",
        "status": "CD"
    },
    {
        "id": 4,
        "title": "Task4 by 1",
        "description": "Finish Task App for Bichitras Task4",
        "status": "CD"
    }
]
```

7. POST /api/tasks/

Request
```
{
    "title": "TaskNew",
    "description": "New Task",
    "status": "NS"
}
```

Response
```
{
    "id": 6,
    "title": "TaskNew",
    "description": "New Task",
    "status": "NS"
}
```

8. PUT /api/tasks/\<id\>/

Request
```
{
    "title": "TaskNew Update",
    "description": "New Task",
    "status": "OG"
}
```
Response
```
{
    "id": 6,
    "title": "TaskNew Update",
    "description": "New Task",
    "status": "OG"
}
```


9. DELETE /api/tasks/\<id\>/

Response
```
{}
```

**Note: Ensurity that only the task owner can view, update, delete task is implemented such that a party cannot access (in any way) the data of other parties.**