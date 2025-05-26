let currentChatId = null;

window.onload = async function() {
  refreshChatList();
};

function startNewChat() {
  const msg = prompt("Start a new chat. Enter your first message:");
  if (!msg) return;
  fetch("/chat/send", {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({chat_id: null, message: msg})
  }).then(res => res.json()).then(data => {
    currentChatId = data.chat_id;
    loadChat(currentChatId);
    refreshChatList();
  });
}

async function refreshChatList() {
  try {
    const res = await fetch("/chat/list");
    if (!res.ok) {
      const text = await res.text();
      console.error("Failed to fetch chat list:", res.status, text);
      return;
    }
    const chats = await res.json();
    const list = document.getElementById("chat-list");
    list.innerHTML = "";
    chats.forEach(chat => {
      const li = document.createElement("li");
      li.innerHTML = `
        <span>${chat.title}</span>
        <small style="display:block;font-size:0.8em;">📅 ${chat.created}</small>
        <button onclick="deleteChat('${chat.id}')">❌</button>
      `;
      li.onclick = () => {
        currentChatId = chat.id;
        loadChat(chat.id);
      };
      list.appendChild(li);
    });
  } catch (err) {
    console.error("Error in refreshChatList:", err);
  }
}

async function deleteChat(chatId) {
  await fetch(`/chat/delete/${chatId}`, { method: "DELETE" });
  if (currentChatId === chatId) currentChatId = null;
  refreshChatList();
  document.getElementById("messages").innerHTML = "";
}

function rewriteImageLinks(markdown) {
  return markdown.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (match, alt, path) => {
    const filename = path.split('/').pop();
    return `![${alt}](/images/${filename})`;
  });
}

async function loadChat(chatId) {
  const res = await fetch(`/chat/load/${chatId}`);
  const data = await res.json();
  const container = document.getElementById("messages");
  container.innerHTML = "";
  currentChatId = chatId;

  data.forEach(msg => {
    if (msg.role === "system") return; // Skip system messages
    const div = document.createElement("div");
    div.className = `message-box message-${msg.role}`;
    const contentWithFixedImages = rewriteImageLinks(msg.content);
    div.innerHTML = marked.parse(contentWithFixedImages);
    container.appendChild(div);
  });
}

async function sendMessage() {
  const input = document.getElementById("chat-input");
  const message = input.value;
  if (!currentChatId) {
    alert("Please select or start a new chat first.");
    return;
  }
  if (!message.trim()) return;

  input.value = "";

  const res = await fetch("/chat/send", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: currentChatId, message })
  });

  const data = await res.json();
  currentChatId = data.chat_id;

  await loadChat(currentChatId);
}
