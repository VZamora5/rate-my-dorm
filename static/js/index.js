const goBtn = document.getElementById("goBtn");

goBtn.addEventListener("click", async () => {
    const input = document.getElementById("search-input");
    const search = input.value.trim(); // remove leading/trailing spaces
    if (!search) return; // ignore empty search

    try {
        const response = await fetch("/search-dorms", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ search })
        });

        const data = await response.json();
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = ""; // clear previous results

        if (data.results.length === 0) {
            const container = document.getElementById("results-container");
            const label = document.createElement("label");
            label.innerHTML = "Could not find results :(";
            
            label.setAttribute("style", "font-family: 'Agdasima', sans-serif; font-size: font-size: 18px; font-weight: 700;")

            container.appendChild(label);
        } else {
            data.results.forEach(dorm => {
                const li = document.createElement("li");
                const a = document.createElement("a");

                // Encode the dorm name safely for URLs
                a.href = "/dorm-review/" + encodeURIComponent(dorm);
                a.textContent = dorm;

                li.appendChild(a);
                resultsDiv.appendChild(li);
        });
        }
    } catch (err) {
        console.error("Error fetching results:", err);
    }
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
