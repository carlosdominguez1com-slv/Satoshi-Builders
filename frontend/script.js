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

document.addEventListener("DOMContentLoaded", () => {
    const convertBtn = document.getElementById("convert");
    const usdInput = document.getElementById("usd");
    const btcResult = document.getElementById("btc-result");
    const satsResult = document.getElementById("sats-result");
    const errorBox = document.getElementById("conv-error");

    convertBtn.addEventListener("click", async function () {

        const usd = parseFloat(usdInput.value);

        btcResult.textContent = "";
        satsResult.textContent = "";
        errorBox.textContent = "";

        if (isNaN(usd) || usd <= 0) {
            errorBox.textContent = "Ingrese un valor válido en USD.";
            return;
        }

        try {
            // Precio de BTC desde Coingecko
            const res = await fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd");

            const data = await res.json();
            
            // ESTA ES LA PARTE CORRECTA
            const btcPrice = data.bitcoin.usd;

            // Conversión USD → BTC
            const btc = usd / btcPrice;

            // Conversión BTC → SATS
            const sats = btc * 100000000;

            btcResult.textContent = `BTC: ${btc.toFixed(8)} BTC`;
            satsResult.textContent = `SATS: ${sats.toFixed(0)} sats`;

        } catch (err) {
            errorBox.textContent = "Error al obtener el precio de Bitcoin.";
        }
    });
});



