// Toggle dark mode by switching Bootstrap classes and saving preference in localStorage
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("darkModeToggle");
    const body = document.body;

    // Check local storage for dark mode preference
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("bg-dark", "text-light");
    }

    // Toggle button click event
    toggleBtn?.addEventListener("click", function () {
        body.classList.toggle("bg-dark");
        body.classList.toggle("text-light");

        // Save preference
        if (body.classList.contains("bg-dark")) {
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.removeItem("darkMode");
        }
    });
});
