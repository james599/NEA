// shows user menu  
function toggleUserMenu() {
    var userMenu = document.getElementById("userMenu");
    userMenu.style.display = (userMenu.style.display === "block") ? "none" : "block";
}

// enter key triggers submit button
var input = document.getElementById("userEntryTextarea");

input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("submitQuery").click();
  }
});

// Select the chat content element
const chatContent = document.getElementById("chatContent");

// Scroll to the bottom of the chat content when the page loads
window.onload = function() {
  chatContent.scrollTop = chatContent.scrollHeight;
};

const sidebar = document.querySelector('.sidebar');
const sidebarToggle = document.querySelector('.sidebar-toggle');
const chatArea = document.querySelector('.chat-area');
const userDropdown = document.querySelector('.user-dropdown');
const entry = document.querySelector('.user-entry');

sidebarToggle.addEventListener('click', () => {
  sidebar.classList.toggle('collapsed');
  chatArea.classList.toggle('collapsed');
  userDropdown.classList.toggle('collapsed')
  sidebarToggle.classList.toggle('collapsed');
  entry.classList.toggle('collapsed')
});

const userMenu = document.querySelector('.user-menu');
const userMenuLinks = document.querySelectorAll('.user-menu a');

userDropdown.addEventListener('click', () => {
  userMenu.classList.toggle('show');
});

userMenuLinks.forEach((link) => {
  link.addEventListener('click', () => {
    userMenu.classList.remove('show');
  });
});
