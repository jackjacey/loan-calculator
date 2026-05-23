async function calculate() {
    const principal = document.getElementById("principal").value;
    const annual_rate = document.getElementById("rate").value;
    const months = document.getElementById("months").value;

    const response = await fetch("https://loan-calculator-production-f61d.up.railway.app/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ principal, annual_rate, months })
    });

    const data = await response.json();
    document.getElementById("monthly").textContent = "$" + data.monthly_payment;
    document.getElementById("total").textContent = "$" + data.total_payment;
    document.getElementById("interest").textContent = "$" + data.total_interest;
    document.getElementById("results").classList.remove("hidden");
}