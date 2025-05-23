function copyOutput(button) {
  const block = button.closest(".prompt-block");
  const code = block.querySelector(".resolved-output").innerText;
  navigator.clipboard.writeText(code);

  const outputBox = document.getElementById("output-box");
  outputBox.value = code;
}