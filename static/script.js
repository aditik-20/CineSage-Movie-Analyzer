async function sendMessage() {
  let input = document.getElementById("message");

  let message = input.value;

  if (message === "") return;

  let mood = document.getElementById("mood").value;

  let chat = document.getElementById("chat-box");

  chat.innerHTML += `<div class="user">${message}</div>`;

  input.value = "";

  const response = await fetch("/chat", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      message: message,
      mood: mood,
    }),
  });

  const data = await response.json();

  chat.innerHTML += `<div class="bot">${data.response}</div>`;

  chat.scrollTop = chat.scrollHeight;
}
