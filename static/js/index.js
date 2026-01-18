const goBtn = document.getElementById("add-recipe");
const input = document.getElementById("recipe-url");
const yield = document.getElementById("servingYield");

// when user searches a recipe
goBtn.addEventListener("click", async () => {
    const recipe_url = document.getElementById("recipe-url")
    let url = recipe_url.value;

    // send POST request to FastAPI
    const response = await fetch("/search-recipe", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            recipe_url: url
        })
    });
    const data = await response.json();
    const input_error = document.getElementById("input-error")
    input_error.textContent = " ";

    // validate data
    if (response.status === 400) {
        input_error.textContent = "Please enter a recipe link!"
    }
    else if (response.status === 404) {
        input_error.textContent = "Unable to find recipe :("
    }
    else if (response.status === 200) {
        // reveal ingredient container
        document.getElementById("ingredient-container").hidden = false;
        const ingredientList = document.getElementById("ingredient-list");
        yield.textContent = data.yields;
        write_list(ingredientList, data.ingredients)
        recipe_url.value = "";
        input_error.textContent = " ";
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
