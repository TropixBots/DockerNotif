import docker
import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

client = docker.from_env()
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
role_id = os.getenv("DISCORD_ROLE_ID")
exclude_raw = os.getenv("EXCLUDE_CONTAINERS", "")
excluded_containers = set(x.strip() for x in exclude_raw.split(",") if x.strip())

def send_discord_message(event_type, container_name, container_id):
    embed = {
        "title": f"Container {event_type}",
        "color": 0x00FF00,
        "fields": [
            {"name": "Container Name", "value": container_name, "inline": False},
            {"name": "Container ID", "value": container_id, "inline": False},
            {"name": "Event Type", "value": event_type, "inline": False},
            {"name": "Timestamp", "value": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()), "inline": False}
        ]
    }
    payload = {
        "content": f"<@&{role_id}>",
        "embeds": [embed]
    }
    requests.post(webhook_url, json=payload)

for event in client.events(decode=True):
    if event["Type"] == "container":
        action = event["Action"]
        container_name = event["Actor"]["Attributes"]["name"]
        container_id = event["id"]
        if container_name in excluded_containers or container_id in excluded_containers or container_id[:12] in excluded_containers:
            continue
        send_discord_message(action, container_name, container_id)
