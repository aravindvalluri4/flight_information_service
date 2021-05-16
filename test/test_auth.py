import unittest
import requests
import os
import string
import random


class AuthApiTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.users = []

    def setUp(self):
        self.api_uri = os.getenv("API_URI","http://localhost:5000/api/v1")
        self.signup_end_point = self.api_uri + "/auth/signup"
        self.login_end_point = self.api_uri + "/auth/login"

    def test_create_new_user_201(self):
        body = {"username": "", "password": "user1_pw"}

        for i in range(5):
            body["username"] = self.genarate_random_user()
            response = requests.post(url=self.signup_end_point, json=body)
            self.assertEqual(201, response.status_code)
            self.assertEqual("user created successfully", self.get_message(response))

    def test_try_create_existing_user_409(self):
        body = {"username": "", "password": "user1_pw"}

        # tyr create existing users
        for username in AuthApiTests.users:
            body["username"] = username
            response = requests.post(url=self.signup_end_point, json=body)
            self.assertEqual(409, response.status_code)
            self.assertEqual("username already taken", self.get_message(response))

    def test_login_200(self):
        body = {"username": "", "password": "user1_pw"}
        for username in AuthApiTests.users:
           body["username"] = username
           response = requests.post(url=self.login_end_point, json=body)
           self.assertEqual(200, response.status_code)
           self.assertEqual("Login Success", self.get_message(response))

    def genarate_random_user(self):
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=6))
        AuthApiTests.users.append(res)
        return res

    def get_message(self, response):
        return response.json()["message"]




