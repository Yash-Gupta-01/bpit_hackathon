const form = document.querySelector("form");
let captcha = document.getElementById("captcha");
const button = document.querySelector("button");

button.disabled = true;

form.addEventListener("keyup", () => {
  let validity = form.checkValidity();
  if (validity === true && captcha.value == 4) {
    button.disabled = false;
  } else {
    button.disabled = true;
  }
});
/*
form.addEventListener("submit", e => {
  e.preventDefault();
  form.innerHTML =
    "<div class='confirmation'>Hi there! This form is currently not connected to any mailscript.</div>";
});
*/
function checkTab(e) {
  if (e.keyCode === 9) {
    button.classList.add("show-outline");
    window.removeEventListener("keydown", checkTab);
  }
}
window.addEventListener("keydown", checkTab);
