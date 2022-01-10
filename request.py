import requests
import os

for file in os.listdir("images"):
    with open("images/" + file, "rb") as f:
        response = requests.post("http://localhost:5000/", files={"file": f})
    print(response.json())
