const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

function appendMessage(content, className) {
    const message = document.createElement('div');
    message.classList.add('message', className);

    if (className === 'bot-message') {
        const container = document.createElement('div');
        container.classList.add('bot-container');
        container.style.display = 'flex';
        container.style.alignItems = 'center';
        container.style.margin = '5px 0';

        const pulpoImg = document.createElement('img');
        pulpoImg.src = './img/Pulpo_S.png';
        pulpoImg.alt = 'Pulpo chatbot';
        pulpoImg.width = 40;
        pulpoImg.style.marginRight = '10px';

        const text = document.createElement('span');
        text.textContent = content;

        container.appendChild(pulpoImg);
        container.appendChild(text);
        message.appendChild(container);
    } else {
        message.textContent = content;
    }

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    appendMessage(userMessage, 'user-message');
    userInput.value = '';

    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage }),
        });

        if (!response.ok) throw new Error('Error al conectar con el servidor.');
        const data = await response.json();
        appendMessage(data.response, 'bot-message');
    } catch (error) {
        console.error('Error:', error.message);
        appendMessage('Hubo un problema al conectar con el servidor.', 'bot-message');
    }
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
