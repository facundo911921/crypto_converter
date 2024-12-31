document.getElementById("convert-form").addEventListener("submit", async function (e) {
    e.preventDefault(); // Evita o recarregamento da página

    const from = document.getElementById("from").value.toUpperCase();
    const to = document.getElementById("to").value.toUpperCase();
    const amount = parseFloat(document.getElementById("amount").value);

    if (!amount || amount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }

    try {
        // Faz a requisição ao backend
        const response = await fetch(`/crypto_price?symbol=${from}&convert_to=${to}`);
        const data = await response.json();

        if (data.error) {
            document.getElementById("result").innerText = `Error: ${data.error}`;
        } else {
            const price = data.price;
            const convertedAmount = (price * amount).toFixed(6);
            document.getElementById("result").innerText = 
                `Converted Amount: ${convertedAmount} ${to} (Rate: ${price} ${to}/${from})`;
        }
    } catch (error) {
        document.getElementById("result").innerText = "An error occurred. Please try again.";
    }
});
