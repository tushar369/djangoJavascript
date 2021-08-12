let box1 = document.getElementById("tbox1");
let box2 = document.getElementById("tbox2");
let box3 = document.getElementById("tbox3");

window.addEventListener("scroll", function () {
  let value = window.scrollY;
  console.log(value);
  if (value <= 460) {
    box1.style.right = 450 + value * -1.05 + "px";
    box2.style.bottom = 480 + value * -1.05 + "px";
    box3.style.left = 450 + value * -1.05 + "px";
  }
});
