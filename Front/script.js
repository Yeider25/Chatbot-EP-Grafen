const chatBox = document.getElementById('chat-area');
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

    // Animación de cargando
    const loadingId = 'loading-' + Date.now();
    appendLoadingMessage(loadingId);

    // Espera la respuesta del backend y al menos 1 segundo
    const fetchPromise = fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(async response => {
        if (!response.ok) throw new Error('Error al conectar con el servidor.');
        return response.json();
    });

    const delayPromise = new Promise(resolve => setTimeout(resolve, 1000));

    try {
        const [data] = await Promise.all([fetchPromise, delayPromise]);
        replaceLoadingMessage(data.response, loadingId);
    } catch (error) {
        console.error('Error:', error.message);
        replaceLoadingMessage('Hubo un problema al conectar con el servidor.', loadingId);
    }
}

function appendLoadingMessage(loadingId) {
    const message = document.createElement('div');
    message.classList.add('message', 'bot-message', 'typing');
    message.id = loadingId;

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

    const dots = document.createElement('span');
    dots.classList.add('loading-dots');
    dots.textContent = 'Cargando';
    const animatedDots = document.createElement('span');
    animatedDots.classList.add('dot-anim');
    dots.appendChild(animatedDots);

    container.appendChild(pulpoImg);
    container.appendChild(dots);
    message.appendChild(container);

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function replaceLoadingMessage(content, loadingId) {
    const loadingMsg = document.getElementById(loadingId);
    if (loadingMsg) {
        loadingMsg.classList.remove('typing');
        loadingMsg.innerHTML = '';
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
        loadingMsg.appendChild(container);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
