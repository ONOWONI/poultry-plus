const roomName = JSON.parse(document.getElementById('room-id').textContent);
const user = document.querySelector("#user")
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/personalchat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(e);
    document.querySelector('#chat-log').value += (data.message + ' - ' +  data.owner + '\n');
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