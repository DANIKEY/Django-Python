

function openNav() {
    document.getElementById("mySidenav").style.width = "330px";
    document.getElementById("page").style.marginLeft = "250px";
    document.getElementById("entete").style.backgroundColor = "white";
    document.getElementById("lien").style.backgroundColor  = "white";
    document.getElementById("lien").style.color = "#036873";
    document.getElementById("lien").onmouseover = function() {
    this.style.backgroundColor = "white";
}


}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("page").style.marginLeft= "auto";
    document.getElementById("entete").style.backgroundColor = "#036873";
    document.getElementById("lien").style.color = "lightblue";
    document.getElementById("lien").style.backgroundColor = "#036873";
    document.getElementById("lien").onmouseover = function() {
    this.style.backgroundColor = "#036873";
}

}