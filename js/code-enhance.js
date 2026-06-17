(function () {
  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn, { once: true });
    } else {
      fn();
    }
  }

  ready(function () {
    document.querySelectorAll("pre").forEach(function (pre) {
      if (pre.closest("figure.highlight") || pre.querySelector(".copy-code-button")) return;
      var button = document.createElement("button");
      button.className = "copy-code-button";
      button.type = "button";
      button.setAttribute("aria-label", "复制代码");
      button.textContent = "copy";
      button.addEventListener("click", function () {
        navigator.clipboard && navigator.clipboard.writeText(pre.innerText || "");
        button.textContent = "done";
        setTimeout(function () {
          button.textContent = "copy";
        }, 1200);
      });
      pre.style.position = "relative";
      pre.appendChild(button);
    });
  });
})();
