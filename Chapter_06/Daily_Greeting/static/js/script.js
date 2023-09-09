// script.js

function myFunction() {
    let today = new Date();
    let hour = today.getHours();
    let minute = today.getMinutes();
    let second = today.getSeconds();
    let message = "";

    if (hour < 12) {
        message = "Good Morning,"
    }
    else if (hour >= 12 && hour <= 18) {
        message = "Good Afternoon,"
    }
    else {
        message = "Good Evening,"
    }

    document.getElementById('greeting').innerHTML = message;
    document.getElementById('time').innerHTML = "The current time is: " + hour + ":" + minute + ":" + second;
}
