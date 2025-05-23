from chat.storage import session_store

def get_chat(chat_id):
    return session_store.load_session(chat_id)
