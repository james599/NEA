function togglePassword() {
    var passwordField = document.getElementById("password");
    var showPasswordToggle = document.querySelector(".show-password");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        showPasswordToggle.textContent = "Hide";
    } else {
        passwordField.type = "password";
        showPasswordToggle.textContent = "Show";
    }
}