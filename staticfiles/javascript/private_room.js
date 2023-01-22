const roomName = JSON.parse(document.getElementById('room-id').textContent);
const user = document.querySelector("#user")
const chatArea = document.querySelector("#chat-area")
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/personalchat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const chatBubble = document.createElement("div")
    const chatMessage = document.createElement("div")
    const chatSender = document.createElement("div")
    const chatTime = document.createElement("div")
    chatBubble.classList.add("chat-bubble")
    chatMessage.id = "chat-message"
    chatSender.id = 'chat-sender'
    chatTime.id = "chat-time"
    if (data.owner === user.textContent) {
        chatBubble.classList.add("right-message")
    }
    chatMessage.innerHTML = data.message
    chatSender.innerHTML = data.owner
    var d = new Date();
    var time = d.toLocaleTimeString();
    chatTime.innerHTML = time
    chatBubble.appendChild(chatSender)
    chatBubble.appendChild(chatMessage)
    chatBubble.appendChild(chatTime)
    chatArea.appendChild(chatBubble)
    // document.querySelector('#chat-log').value += (data.message + ' - ' +  data.owner + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'owner': user.textContent
    }));
    messageInputDom.value = '';
};