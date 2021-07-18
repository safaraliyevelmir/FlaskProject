var menu =document.getElementById("menu");
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  }