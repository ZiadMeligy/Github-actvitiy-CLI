import requests

# Get data from GitHub API
response = requests.get('https://api.github.com/users/ZiadMeligy/events')
data = response.json()


repo_events = {}

for event in data:
    repo_name = event['repo']['name']


    if repo_name not in repo_events:
        repo_events[repo_name] = {"PushEvent": 0, "CreateEvent": 0, "DeleteEvent": 0}


    if event["type"] == "PushEvent":
        repo_events[repo_name]["PushEvent"] += 1
    elif event["type"] == "CreateEvent":
        repo_events[repo_name]["CreateEvent"] += 1
    elif event["type"] == "DeleteEvent":
        repo_events[repo_name]["DeleteEvent"] += 1

for key,x in repo_events.items():
    print("Repository name:" + key)
    print("Pushes:" + str(x["PushEvent"]))
    print("Creations" +str(x["CreateEvent"]))

