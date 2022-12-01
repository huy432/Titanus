function menubar_toggle(){
    const menu = document.getElementById("menu-bar")
    menu.classList.toggle("menu-bar-active")
    menu.classList.toggle("menu-bar-unactive")
}
function openText(){
    const oP = document.getElementById("open-text");
    const oL = document.getElementsByClassName("movie-content-preview-data")
    const btn = document.getElementsByClassName("movie-content-preview-button")
    oP.classList.toggle("open-text")
    oL[0].classList.toggle("active")
    if (oL[0].classList.contains("active")){
        btn[0].textContent = "Thu gọn..";
    }
    else{
        btn[0].textContent = "Mở rộng..";
    }
}
