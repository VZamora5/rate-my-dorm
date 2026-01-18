const goBtn = document.getElementById("goBtn");

goBtn.addEventListener("click", async () => {
    console.log("search");
    const input = document.getElementById("search-input");
    const search = input.value;

    // Send POST request to FastAPI endpoint /search-dorms
    const response = await fetch("/search-dorms", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ search })
    });

    // Parse JSON response
    const data = await response.json();

    // Log results (or display them in your page)
    console.log(data);

    // Optional: display results in a div
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = ""; // clear previous results
    data.results.forEach(dorm => {
        const p = document.createElement("p");
        p.textContent = dorm;
        resultsDiv.appendChild(p);
    });
});

document.addEventListener("keydown", (e) => {
    if (e.key == "Enter" && input === document.activeElement) {
        goBtn.classList.add("press"); // Simulate button click
        goBtn.click();
    }
});

document.addEventListener("keyup", (e) => {
    if (e.key == "Enter") {
        goBtn.classList.remove("press"); // Simulate button click
    }
});
