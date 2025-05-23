import uuid
from chat.storage import session_store
from openai import OpenAI
import os

# --- Add below ---
from chat.storage.session_store import validate_image_filenames
validate_image_filenames()
# --- end add ---

# Initialize client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def process_message(chat_id, user_message):
    # New chat?
    if not chat_id:
        chat_id = session_store.create_session(user_message)
        session = [{"role":"system","content":"You are a helpful assistant."},
                   {"role":"user","content": user_message}]
    else:
        session = session_store.load_session(chat_id)
        session.append({"role": "user", "content": user_message})

    # GPT-4o API call
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=session
    )
    assistant_reply = response.choices[0].message.content

    # Persist and return
    session.append({"role": "assistant", "content": assistant_reply})
    session_store.save_session(chat_id, session)

    return {"chat_id": chat_id, "response": assistant_reply}
