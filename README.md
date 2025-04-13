# fastapi-service-template


### Install and run on Local:
```shell
pip install -r requirements.txt
python main.py
```

### Docker build and run:
```shell
docker build -t rest-service:v1 . 
docker run -d --name rest-sercvice -p 8000:8000 rest-service:v1
```
