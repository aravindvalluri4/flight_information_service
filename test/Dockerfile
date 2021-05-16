From python:3.9

RUN pip install requests

ENV API_URI=http://localhost:5000/api/v1

COPY . /test
WORKDIR /test
CMD ["python", "-m", "unittest", "discover"]

