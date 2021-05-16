import unittest
import requests
import os
import string
import random


class FlightApiTests(unittest.TestCase):


    def setUp(self):
        # initialize end points
        self.api_uri = os.getenv("API_URI","http://localhost:5000/api/v1")
        self.flights_end_point = self.api_uri + "/flights"
        self.signup_end_point = self.api_uri + "/auth/signup"
        self.login_end_point = self.api_uri + "/auth/login"

        # create user
        self.user = self.genarate_random_string()
        self.password = "password_1"
        body = {"username": self.user, "password": self.password}
        response = requests.post(url=self.signup_end_point, json=body)
        self.assertEqual(201, response.status_code)
        self.assertEqual("user created successfully", self.get_message(response))


        # login user
        response = requests.post(url=self.login_end_point, json=body)
        self.assertEqual(200, response.status_code)
        self.assertEqual("Login Success", self.get_message(response))
        self.token =  "Bearer " + response.json()["token"]
        
    def test_create_new_flight_201(self):
        self.create_flight()

    def test_create_new_flight_unauthorized_401(self):
        body = self.get_new_flight()
        response = requests.post(url=self.flights_end_point,
                                 json=body)
        self.assertEqual(401, response.status_code)

    def test_get_flight_200(self):
        # create flight
        id = self.create_flight()

        # get flight
        code, body = self.get_flight(id)
        self.assertEqual(200, code)
        self.assertEqual(id, body["id"])

    def test_get_flight_404(self):
        # send some invalid id
        id = "123e4567-e89b-12d3-a456-426614174000"
        code, body = self.get_flight(id)
        self.assertEqual(404, code)

    def test_update_flight_200(self):
        # create a flight
        id = self.create_flight()

        # update fare to 20
        body = {"fare":"20"}
        response = requests.put(url=self.get_url_id(id),
                                 json=body,
                                 headers={"Authorization": self.token})
        self.assertEqual(200, response.status_code)
        self.assertEqual("updated successfully", self.get_message(response))

        # verify fare is updated
        code, body = self.get_flight(id)
        self.assertEqual("20.00",body["fare"])

    def test_update_flight_200(self):
        # create a flight
        id = self.create_flight()

        # check flight exists
        code, body = self.get_flight(id)
        self.assertEqual(200, code)

        # delete flight
        response = requests.delete(url=self.get_url_id(id),
                                 headers={"Authorization": self.token})
        self.assertEqual(200, response.status_code)
        self.assertEqual("deleted successfully", self.get_message(response))

        # check flight does not exists
        code, body = self.get_flight(id)
        self.assertEqual(404,code)

    def genarate_random_string(self):
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=6))
        return res

    def get_message(self, response):
        return response.json()["message"]

    def get_new_flight(self):
        return {
            "fare": "2000.00",
            "flight_duration_mins": 320,
            "destination": "stockholm",
            "arrival_date_time": "2021-02-04 20:05:06",
            "departure": "hyderabad",
            "flight_number": 555,
            "flight_name": self.genarate_random_string(),
            "schedule_date_time": "2021-02-04 04:05:06"
        }

    def create_flight(self):
        body = self.get_new_flight()
        response = requests.post(url=self.flights_end_point,
                                 json=body,
                                 headers={"Authorization": self.token})
        self.assertEqual(201, response.status_code)
        self.assertEqual("new flight created", self.get_message(response))
        return response.json()["id"]

    def get_url_id(self, id):
        return self.flights_end_point + "/" + id

    def get_flight(self, id):
        response = requests.get(url=self.get_url_id(id),
                                headers={"Authorization": self.token})
        if response.status_code == 200:
            return 200, response.json()
        else:
            return response.status_code, ""










