import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")


def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())
