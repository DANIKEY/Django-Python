function UpdateProcedure(){
  var str = document.forms["myForm"]["procedure"].value;
  var url = "http://127.0.0.1:8000/updateProcedure/"+str+"";
  document.location.href = url;
}


function deleteProcedure(){
  var str = document.forms["myForm"]["procedure"].value;
  var url = "http://127.0.0.1:8000/supprimerProcedure/"+str+"/"+2;
  document.location.href = url;
}


function AfficheProcedure(){
   var str = document.forms["myForm"]["procedure"].value;
  
  if(str==""){
    document.getElementById("txtHint").innerHTML = ""
    return;

  }else {
        if (window.XMLHttpRequest) {
            // Code pour IE7+, Firefox, Chrome, Opera, Safari
            xmlhttp = new XMLHttpRequest();
        } else {
            // code pour IE6, IE5
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("txtHint").innerHTML = this.responseText;
            }
        };
        xmlhttp.open("GET","http://127.0.0.1:8000/afficheProcedureId/"+str,true);
        xmlhttp.send();
    }
}
    var x, i, j, selElmnt, a, b, c;
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
 
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
 
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 0; j < selElmnt.length; j++) {
    
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
       
        var i, s, h;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        h = this.parentNode.previousSibling;
        for (i = 0; i < s.length; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            break;
          }
        }
        h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
      
      AfficheProcedure();
      e.stopPropagation();
      closeAllSelect(this);
      this.nextSibling.classList.toggle("select-hide");
      this.classList.toggle("select-arrow-active");
    });
}
function closeAllSelect(elmnt) {
  
  var x, y, i, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  for (i = 0; i < y.length; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < x.length; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);


function openNav() {
    document.getElementById("mySidenav").style.width = "330px";
    document.getElementById("pageSelection").style.marginLeft = "250px";
    document.getElementById("entete").style.backgroundColor = "white";
    document.getElementById("lien").style.backgroundColor  = "white";
    document.getElementById("lien").style.color = "#036873";
    document.getElementById("lien").onmouseover = function() {
    this.style.backgroundColor = "white";
}

}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("pageSelection").style.marginLeft= "auto";
    document.getElementById("entete").style.backgroundColor = "#036873";
    document.getElementById("lien").style.color = "lightblue";
    document.getElementById("lien").style.backgroundColor = "#036873";
    document.getElementById("lien").onmouseover = function() {
    this.style.backgroundColor = "#036873";
}


}
