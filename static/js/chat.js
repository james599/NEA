function toggleUserMenu() {
    var userMenu = document.getElementById("userMenu");
    userMenu.style.display = (userMenu.style.display === "block") ? "none" : "block";
}

var input = document.getElementById("queryInput");

input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("submitQuery").click();
  }
});