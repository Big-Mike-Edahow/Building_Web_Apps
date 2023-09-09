// script.js

function myFunction(id) {
    let userName=document.getElementById("nameId").value;
    let buttonClicked=document.getElementById(id).name;

    if (buttonClicked == "button1") {
        alert("Of course you can vote, " + userName + "! Cheers! 👏👏");
    }
    else {
        alert("No voting rights for you yet, " + userName + ". 🙅");
    }
}

