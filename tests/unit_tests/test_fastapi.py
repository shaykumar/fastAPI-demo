#! /usr/bin/python3

"""
Test for the main page using fastapi.testclient.
"""
import os
import sys
from fastapi.testclient import TestClient

print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

sys.path.append("/home/ec2-user/fastAPI-demo/")

print(sys.path)

from main import app

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Declaring test client
client = TestClient(app)

# Test for status code for get message
def test_get_home_url():
    response = client.get("/")
    assert response.status_code == 200
