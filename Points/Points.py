import json
from pprint import pprint

with open("Points/UserPoints.json") as f:
    data = json.load(f)

def findUserPoints(user):
    if(data[user]):
        return data[user]["points"]
    else :
        data[user]["points"] = {0}

def addPoints(user):
    if(data[user]):
        data[user]["points"] = data[user]["points"] + 10
    else :
        data[user]["points"] = {0}

