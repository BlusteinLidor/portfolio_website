console.log("Hello world");
window.alert("HAHA")

let age = 25;
console.log(age);

document.getElementById("p1").innerHTML = "Hello " + age;
let username = window.prompt("What's your name?");
console.log(username);

document.getElementById("myButton").onclick = function(){
    username = document.getElementById("myText").value;
    document.getElementById("myLabel").innerHTML = "Hello";
    console.log(username);
    
}