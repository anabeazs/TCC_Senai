const ham =document.querySelector(".hamburger")
const navBar = document.querySelector(".links")

ham.addEventListener("click",()=>{
    ham.classList.toggle("active")
    navBar.classList.toggle("active")

})