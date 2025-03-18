const button = document.getElementById("button");

button.addEventListener("click", function () {
    const cityInput = document.getElementById("cityInput");
    console.log("Button is clicked.", cityInput.value);

    get_data(cityInput.value);  // Pass the city value to get_data function

    cityInput.value = "";  // Clear input after clicking
});

function get_data(city) {
    fetch("http://127.0.0.1:5000/get_weather", {  // Use correct API endpoint
        method: "POST",  // Use POST method
        headers: {
            "Content-Type": "application/json"  // Tell server you're sending JSON data
        },
        body: JSON.stringify({ city: city })  // Send city name as JSON
    })
    .then(response => response.json()) // Convert response to JSON
    .then(data => {
        console.log("API Response:", data);  // Log the API response
    
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
}
