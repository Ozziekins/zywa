document.getElementById("userMobileBtn").onclick = function() {
    promptForInputAndFetchStatus("user_mobile");
};

document.getElementById("cardIdBtn").onclick = function() {
    promptForInputAndFetchStatus("card_id");
};

function promptForInputAndFetchStatus(type) {
    const input = prompt(`Enter ${type.replace('_', ' ')}:`);
    if (input) {
        fetch('/get_card_status', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ [type]: input })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("statusDisplay").textContent = `error: ${data.error}`;
            } else {
                document.getElementById("statusDisplay").textContent = `status: ${data.status}`;
            }
        })
        .catch(error => console.error('Error:', error));
    }
}
