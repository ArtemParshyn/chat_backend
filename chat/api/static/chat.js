let new_div;
const div_chat_body = document.getElementById("chat_body");
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const author = JSON.parse(document.getElementById('user-name').textContent);
console.log("author: " + author);

chatSocket.onmessage = function(e) {
    data = JSON.parse(e.data);
    new_div = document.createElement('div');
    new_div.innerHTML = "author - " + data.author + " message - " + data.message + "\n\n";
    div_chat_body.appendChild(new_div);
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
    messageInputDom.value = "";
    console.log(JSON.stringify({"message": message, "author": author}));
    chatSocket.send(JSON.stringify({
        'author': author,
        'message': message,
        'exclude_myself': true,
    }));
};