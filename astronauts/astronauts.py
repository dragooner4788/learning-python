'''
Description: using the Open Notify system which we can gather details about the international Space Station
Why: I am doing this to learn more about APIs and how to use them in Python. 
Date: 2/9/2021 10:43PM
'''


import requests
import json


# Getting information about the astronauts on the ISS right now.
response = requests.get("http://api.open-notify.org/astros.json")


def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())


location_iss_parameters = {  # parameters to pass to the request we are making.
    "lat": 40.4406,
    "lon": 79.9959
}
location_iss = requests.get(
    # request made to open notify.
    "http://api.open-notify.org/iss-pass.json", params=location_iss_parameters
)

# We are just getting the response key from the dictionary/json we get back.
pass_times = location_iss.json()['response']
jprint(pass_times)

risetimes = []

for risestime in pass_times:
    time = risestime['risetime']
    risetimes.append(time)

for risetime in risetimes:
    print(f"Rise Time: {risestime['risetime']}")
