var navbarvertical =document.getElementById("navt");
        
navbarvertical.style.height ='0%';
function toggle() {
   
    if(navbarvertical.style.height=='0%'){
        navbarvertical.style.height='50%';
    }
    else{
        navbarvertical.style.height='0%';
    }
   
}






let myInput = document.getElementById("myInput");

// Gestionnaire d'événement pour la saisie dans la zone de texte
myInput.addEventListener("input", function () {
    let inputvalue = myInput.value.toUpperCase();

    // Afficher/masquer le menu vertical en fonction de la saisie
    toggle();

    // Filtrer les éléments en fonction de la saisie
    let latestCol = document.getElementsByClassName("latest-col");
    Array.from(latestCol).forEach(function (element) {
        let Coltxt = element.getElementsByTagName("h3")[0].innerText.toUpperCase();
        if (Coltxt.includes(inputvalue)) {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    });

})