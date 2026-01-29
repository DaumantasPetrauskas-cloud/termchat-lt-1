document.addEventListener('DOMContentLoaded', () => {
    // --- DOM ELEMENTS ---
    const input = document.getElementById('command-input');
    const output = document.getElementById('output');
    const introScreen = document.getElementById('intro-screen');
    const chatRoom = document.getElementById('chat-room');
    const statusText = document.getElementById('status-text');

    // --- STATE ---
    let isJoined = false;

    // --- FOCUS INPUT AUTOMATICALLY ---
    // Keeps the cursor in the input box so the user doesn't have to click it
    input.focus();

    // Listen for clicks anywhere to refocus input (good for UX)
    document.addEventListener('click', () => {
        input.focus();
    });

    // --- EVENT LISTENER FOR INPUT ---
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const text = input.value.trim();

            if (!isJoined) {
                // If not joined, any Enter key attempts to join
                joinRoom();
            } else {
                // If joined, process the command/message
                if (text) {
                    processMessage(text);
                }
            }
            
            // Clear input after processing
            input.value = '';
        }
    });

    // --- FUNCTION: JOIN ROOM ---
    function joinRoom() {
        isJoined = true;
        
        // Hide intro, show chat
        introScreen.classList.add('hidden');
        chatRoom.classList.remove('hidden');
        
        // Update status
        statusText.innerText = "🔊 Connected";
        statusText.style.color = "#33ff00";
        statusText.style.animation = "none";

        // Add a welcome message
        addSystemMessage("Connection established.");
        
        // Scroll to bottom
        scrollToBottom();
    }

    // --- FUNCTION: PROCESS MESSAGE ---
    function processMessage(text) {
        // 1. Display User's Message
        addMessage(`You: ${text}`, 'user-msg');

        // 2. SIMULATE BACKEND/SOCKET RESPONSE
        // Since we don't have the real backend, we simulate a reply.
        // Replace this logic with your actual socket.emit() or fetch() call.
        simulateBotReply(text);
        
        scrollToBottom();
    }

    // --- FUNCTION: ADD MESSAGE TO SCREEN ---
    function addMessage(text, className) {
        const p = document.createElement('p');
        p.textContent = text; // textContent prevents HTML injection (XSS)
        p.className = className;
        chatRoom.appendChild(p);
    }

    function addSystemMessage(text) {
        const p = document.createElement('p');
        p.textContent = text;
        p.className = 'system-msg';
        chatRoom.appendChild(p);
    }

    // --- HELPER: SCROLL TO BOTTOM ---
    function scrollToBottom() {
        output.scrollTop = output.scrollHeight;
    }

    // --- MOCK: SIMULATE REPLY (Replace with real backend) ---
    function simulateBotReply(userText) {
        // Simple echo bot logic for demonstration
        setTimeout(() => {
            const reply = `System: Received "${userText}"`;
            addMessage(reply, 'other-msg');
            scrollToBottom();
        }, 600 + Math.random() * 1000); // Random delay
    }
});
