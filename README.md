build an app
```bash
docker-compose up --build
```

registration
```bash
curl http://127.0.0.1:8000/register/ -X POST -d "username=<username>&password=<password>&email=<email>"
```

get token
```bash
curl http://127.0.0.1:8000/get_token/ -X POST -d "username=<username>&password=<password>"
```

create app
```bash
curl http://127.0.0.1:8000/create_app/ -H 'Authorization: Token <Token>' -X POST -d "name=<app_name>"
```

change app
```bash
curl http://127.0.0.1:8000/change_app/ -H 'Authorization: Token <Token>' -X POST -d "api_key=<api key for app>&name=<info>&info=<info>"
```

get info about app
```bash
curl http://127.0.0.1:8000/api/test/ -H 'Authorization: Token <Token>' -X GET -d "api_key=<api key for app>"
```

delete app
```bash
curl http://127.0.0.1:8000/delete_app/ -H 'Authorization: Token <Token>' -X POST -d "api_key=<api key for app>"
```
