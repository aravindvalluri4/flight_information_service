## Flights Informations Service 1.0.0

Flight information service provides information of flights between cities. It allows
various operation to add/delete/update&view flight information. User should be
authenticated to utilize this services. User can signup and login using
this service. Ideal design would be to have different services for flight information
and security services(signup, login). But for now its desgined in same service.
Postgres is used as backend and JWT is used for authorization.

For further details on API refer to RAML specifications in doc/service.html


#### Table of contents

1. [Environment Setup](#envsetup)
1. [Build](#build)
1. [Install](#install)
1. [Testing](#testing)
1. [Usage Examples](#usage)


### <a name="envsetup"></a> Environment Setup

Ensure docker  and docker-compose are installed.

```bash
sudo service docker status
```
Install Python3 & virtual env for development.


### <a name="build"></a> Build

1. Update POSTGRES_PASWORD & JWT_SECRET_KEY environment variables of docker-compose.yaml.
2. Ideally use docker/kubernetes secretes for above task, but for now its desgined in this way.
3. Build image by executing below command in porject root level(flight_information_service).

```bash
docker build -f Dockerfile . -t flights_service:1.0
```
### <a name="install"></a> Install

use docker-compose up to start application instance. Below command installs
flight_service and postgres as backend service to store and retreive data

```bash
docker-compose up -d
```

to troubleshoot and check logs

```bash
docker-compose logs
```

### <a name="testing"></a> Testing

1. python unittest is used.
2. Build and install service.

Test in docker

```bash
cd test
docker build -f Dockerfile . -t flights_tests:1.0
docker run --network=host --rm -ti flights_tests:1.0
```

Test outside docker

```bash
export API_HOT="host"
python -m unittest -v
```

### <a name="usage"></a> Usage Examples

For API description and usage examples, please refer to api secps.


```bash
firefox service.html&
```
