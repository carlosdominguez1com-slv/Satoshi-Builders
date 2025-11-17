// Generar Invoice
document.getElementById("btn").addEventListener("click", async () => {
    const amount = document.getElementById("amount").value;

    try {
        const res = await fetch("http://localhost:5000/api/invoice", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ amount: parseInt(amount) })
        });

        if (!res.ok) throw new Error("Error al conectar con el backend");

        const data = await res.json();

        document.getElementById("qr").innerHTML =
            `<img src="data:image/png;base64,${data.qr_base64}">`;

        document.getElementById("payreq").textContent = data.payment_request;
    } 
    catch (error) {
        console.error("Fallo:", error);
        alert("Error: No se pudo conectar con el backend");
    }
});

document.getElementById("convert").addEventListener("click", async () => {
    const usd = document.getElementById("usd").value;
    const result = document.getElementById("btc-result");
    const errorBox = document.getElementById("conv-error");

    result.textContent = "";
    errorBox.textContent = "";

    if (!usd || usd <= 0) {
        errorBox.textContent = "Ingrese una cantidad válida";
        return;
    }

    try {
        // API QUE SÍ FUNCIONA
        const res = await fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd");

        if (!res.ok) throw new Error("Falló la API");

        const data = await res.json();
        const price = data.bitcoin.usd; // precio en USD

        const btc = usd / price;

        result.textContent = `${usd} USD = ${btc.toFixed(8)} BTC`;
    } 
    catch (err) {
        errorBox.textContent = "No se pudo obtener el precio. Verifique su conexión.";
        console.error(err);
    }
});
