import os
import json
import uuid
from datetime import datetime
from collections import defaultdict


base_path = "files/chat_sessions"

def create_session(first_msg):
    chat_id = str(uuid.uuid4())
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    session_data = {
        "created": datetime.utcnow().isoformat(),
        "messages": [{"role": "user", "content": first_msg}]
    }
    with open(os.path.join(base_path, f"{chat_id}.json"), "w") as f:
        json.dump(session_data, f)
    return chat_id


def load_session(chat_id):
    path = os.path.join(base_path, f"{chat_id}.json")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        data = json.load(f)
    return data["messages"]


def save_session(chat_id, messages):
    path = os.path.join(base_path, f"{chat_id}.json")
    with open(path) as f:
        data = json.load(f)
    data["messages"] = messages
    with open(path, "w") as f:
        json.dump(data, f)


def validate_image_filenames():
    seen = defaultdict(list)
    for root, _, files in os.walk("files/images"):
        for fname in files:
            seen[fname].append(os.path.join(root, fname))
    duplicates = {k: v for k, v in seen.items() if len(v) > 1}
    if duplicates:
        raise ValueError(
            "Duplicate image filenames detected:\n" +
            "\n".join(f"{k}: {v}" for k, v in duplicates.items())
        )
