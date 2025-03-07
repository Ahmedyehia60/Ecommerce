const bar = document.getElementById("bar");
const close = document.getElementById("close");
const nav = document.getElementById("navbar");

if (bar) {
  bar.addEventListener("click", () => {
    nav.classList.add("active");
  });
}

if (close) {
  close.addEventListener("click", () => {
    nav.classList.remove("active");
  });
}

// active page link on click

const links = document.querySelectorAll("#navbar a");

function activeLinks() {
  links.forEach((link) => {
    link.classList.remove("active");
    if (link.href === window.location.href) {
      link.classList.add("active");
    }
  });

  links.foreach((link) => {
    link.addEventListener("click", function () {
      activeLinks();
    });
  });
}

activeLinks();

document.querySelectorAll(".pro").forEach((div) => {
  div.addEventListener("click", (e) => {
    if (!e.target.closest("a")) {
      window.location.href = "single_product.html";
    }
  });
});
