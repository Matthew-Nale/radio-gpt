document.addEventListener('DOMContentLoaded', function () {
    const queryLocation = document.getElementById('query-location');
    const userQueryInput = document.getElementById('user-query-input');
    const conversationArea = document.getElementById('conversation-area')
    const submitQueryURL = '/api/chat'
    var isFirstQuery = true;

    userQueryInput.addEventListener('keydown', function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
        }
    });

    userQueryInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && userQueryInput.value) {

            if (isFirstQuery) {
                isFirstQuery = false;
                queryLocation.style.top = 'auto';
                queryLocation.style.bottom = '5vh';
            }

            const conversation = {query: userQueryInput.value}
            createUserMessage(userQueryInput.value)
            userQueryInput.value = '';

            axios.post(submitQueryURL, conversation)
            .then(response => response.data)
            .then(data => {
                createResponseMessage(data.message)
            });
        }
    });

    function createUserMessage(message) {
        const element = document.createElement('div');
        element.innerHTML = message
        element.setAttribute('class', 'user-message');
        conversationArea.appendChild(element);
    }

    function createResponseMessage(message) {
        const element = document.createElement('div');
        element.innerHTML = message
        element.setAttribute('class', 'response-message');
        conversationArea.appendChild(element);
    }

});