let section = document.querySelector('section');
let group1 = document.getElementById("group1");
let group2 = document.getElementById("group2");
let messages = document.getElementById("messages");
let messageBox = document.getElementById("message");
let sendButton = document.getElementById("sendButton");
let currentRoom = null;

let socket = io("http://localhost:5000");
let username = window.prompt("USERNAME: ");;


socket.on('connect', () => {
    console.log('<-------CONNECTED------->');
});

socket.on('disconnect', () => {
    console.log('<-------DISCONNECTED------->');
});

socket.on('new_message', (data) => {
    console.log(data);
    let p = document.createElement('p');
    p.innerHTML = data['username'] + ": " + data['message'];
    messages.appendChild(p);
})


group1.addEventListener('click', () => {
    currentRoom = 'group1';
    socket.emit('join', {
        username: username,
        room: currentRoom
    });
});
group2.addEventListener('click', () => {
    currentRoom = 'group2';
    socket.emit('join', {
        username: username,
        room: currentRoom
    });
});
sendButton.addEventListener('click', () => {
    let text = messageBox.value;
    messageBox.value = "";
    socket.emit('new_message', {
        username: username,
        message: text,
        room: currentRoom
    });
});
