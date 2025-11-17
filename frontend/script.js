document.getElementById("btn").addEventListener("click", async () => {
    const amount = document.getElementById("amount").value;

    try {
        const res = await fetch("http://localhost:5000/api/invoice", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ amount: parseInt(amount) })
        });

        if (!res.ok) {
            throw new Error("Error al conectar con el backend");
        }

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


