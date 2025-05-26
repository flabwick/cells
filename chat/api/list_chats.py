import os
import json
from datetime import datetime

def get_chat_summaries():
    summaries = []
    path = "files/chat_sessions"
    for fname in os.listdir(path):
        if not fname.endswith(".json"):
            continue
        chat_id = fname.replace(".json", "")
        with open(os.path.join(path, fname)) as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    messages = data
                    created = "unknown"
                else:
                    messages = data.get("messages", [])
                    created = data.get("created", "unknown")

                # Find first user message only
                title = next((m["content"][:100] for m in messages if m["role"] == "user"), "Untitled")

                if created != "unknown":
                    created = datetime.fromisoformat(created).strftime("%Y-%m-%d %H:%M")

                summaries.append({
                    "id": chat_id,
                    "title": title,
                    "created": created
                })
            except Exception as e:
                print(f"Error loading chat {chat_id}: {e}")
    return summaries
