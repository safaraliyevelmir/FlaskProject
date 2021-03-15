function myFunction() {
    document.getElementById("menu1").style.display = "none";
    document.getElementById("menu2").style.display = "block"
    document.getElementById("menu4").style.display = "none"
    document.getElementById("menu5").style.display = "none"
    document.getElementById("menu3").style.display = "none"
    document.getElementById("btn2").style.color = "#d81300"
    document.getElementById("btn5").style.color = "black"
    document.getElementById("btn3").style.color = "black"
    document.getElementById("btn4").style.color = "black"
   
}
function myFunction2() {
    document.getElementById("menu1").style.display = "block"
    document.getElementById("menu2").style.display = "none"
    document.getElementById("menu5").style.display = "none"
    document.getElementById("menu4").style.display = "none"
    document.getElementById("menu3").style.display = "none"
    document.getElementById("btn5").style.color = "black"
    document.getElementById("btn2").style.color = "black"
    document.getElementById("btn3").style.color = "black"
    document.getElementById("btn4").style.color = "black"
}
function myFunction3() {
    document.getElementById("menu1").style.display = "none"
    document.getElementById("menu2").style.display = "none"
    document.getElementById("menu5").style.display = "none"
    document.getElementById("menu4").style.display = "none"
    document.getElementById("menu3").style.display = "block"
    document.getElementById("btn3").style.color = "#d81300"
    document.getElementById("btn2").style.color = "black"
    document.getElementById("btn5").style.color = "black"
    document.getElementById("btn4").style.color = "black"
    
}
function myFunction4() {
  document.getElementById("menu1").style.display = "none"
  document.getElementById("menu2").style.display = "none"
  document.getElementById("menu5").style.display = "none"
  document.getElementById("menu3").style.display = "none"
  document.getElementById("menu4").style.display = "block"
  document.getElementById("btn2").style.color = "black"
  document.getElementById("btn5").style.color = "black"
  document.getElementById("btn4").style.color = "#d81300"
  document.getElementById("btn3").style.color = "black"
  
}
function myFunction5() {
    document.getElementById("menu1").style.display = "none"
    document.getElementById("menu2").style.display = "none"
    document.getElementById("menu3").style.display = "none"
    document.getElementById("menu4").style.display = "none"
    document.getElementById("menu5").style.display = "block"
    document.getElementById("btn5").style.color = "#d81300"
    document.getElementById("btn2").style.color = "black"
    document.getElementById("btn3").style.color = "black"
    document.getElementById("btn4").style.color = "black"
    
}
  

function filter() {
  var elems = document.getElementsByClassName( 'other' );
  for ( var i = 0, l = elems.length; i < l; i++ )
    elems[ i ].style.display = 'block';
  var elems = document.getElementsByClassName( 'cv' );
  for ( var i = 0, l = elems.length; i < l; i++ )
     elems[ i ].style.display = 'block';
  document.getElementById("all1").style.color = "#d81300"
  document.getElementById("cv1").style.color = "#787878"
  document.getElementById("other1").style.color = "#787878"

}
function filter2() {
    var elems = document.getElementsByClassName( 'other' );
    for ( var i = 0, l = elems.length; i < l; i++ )
      elems[ i ].style.display = 'none';
    var elems = document.getElementsByClassName( 'cv' );
    for ( var i = 0, l = elems.length; i < l; i++ )
       elems[ i ].style.display = 'block';
    document.getElementById("all1").style.color = "#787878"
    document.getElementById("cv1").style.color = "#d81300"
    document.getElementById("other1").style.color = "#787878"

  }
  function filter3() {
    var elems = document.getElementsByClassName( 'cv' );
    for ( var i = 0, l = elems.length; i < l; i++ )
      elems[ i ].style.display = 'none';
    var elems = document.getElementsByClassName( 'other' );
    for ( var i = 0, l = elems.length; i < l; i++ )
       elems[ i ].style.display = 'block';
    document.getElementById("all1").style.color = "#787878"
    document.getElementById("cv1").style.color = "#787878"
    document.getElementById("other1").style.color = "#d81300"

  }

function openmenu() {
    var element = document.getElementById("openmenu");
    element.classList.remove("close");
    element.classList.add("open");
    }
