'use strict'

//Parte Visualización de skins
let contenedorSkins = document.getElementById('skins');
let skins = document.querySelectorAll(".link-skin");

skins.forEach(item=>{
    let divSkin = document.createElement('div');
    divSkin.className = "skin";
    divSkin.appendChild(item);
    contenedorSkins.appendChild(divSkin);
});


