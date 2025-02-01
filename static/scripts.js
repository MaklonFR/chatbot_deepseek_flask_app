document.getElementById("send-button").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    // Add user message to chat box
    addMessage(userInput, "user");

    // Clear input field
    document.getElementById("user-input").value = "";

    // Send user message to Flask
    fetch('/get_response', {
        method: 'POST',
        body: new URLSearchParams({
            'message': userInput
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        addMessage(data.response, "bot");
    });
});

function addMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(sender);
    messageDiv.innerText = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}