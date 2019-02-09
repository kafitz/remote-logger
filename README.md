remote-logger
=============
A quick and dirty solution for logging in difficult situations like the capturing of raw request payloads from an API sitting in a container behind a large cloud provider's load balancer.

#### Steps:
1. Setup a mongodb instance within a container connected to the host network on the traditional port 27017 and hostname configured as `mongo`
2. Clone this repository
3. Build the Docker container: `docker build -t remote-logger .`
4. Run the container: `docker run -e MONGO_HOST=mongo -e MONGO_DATABASE=mobile_api_logs -e MONGO_USERNAME=root -e MONGO_PASSWORD=password -p 8000:8000 -t --name remote-logger remote-logger:latest`
    - add `--link mongo:mongo` if running to debug from OSX

Place a snippet of code like this within the Python source to log:
```python
from threading import Thread
import requests
def log_request(data):
    def _async_push(data):
        r = requests.post('http://<destination.server>/log', json=data)
        assert r.status_code == 201

    t = Thread(target=_async_push, args=(data,))
    t.daemon = True
    t.start()
```
