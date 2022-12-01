function menubar_toggle(){
    const menu = document.getElementById("menu-bar")
    menu.classList.toggle("menu-bar-active")
    menu.classList.toggle("menu-bar-unactive")
}
function light(){
    const a = document.getElementById("lightbulb");
    const b = document.getElementById("bulb");
    a.classList.toggle("active");
    if (a.classList.contains("active")){
        b.style.display = "block";
        a.innerText = "Light: Off";
    }
    else{
        b.style.display = "none";
        a.innerText = "Light: On";
    }
}