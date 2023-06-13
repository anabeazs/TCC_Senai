// const ham =document.querySelector(".hamburger")
// const navBar = document.querySelector(".links")

// ham.addEventListener('click',()=>{
//     ham.classList.toggle('active')
//     navBar.classList.toggle('active')

// });


var onda1 = document.getElementById('onda1')
var onda2 = document.getElementById('onda2')
var onda3 = document.getElementById('onda3')
var onda4 = document.getElementById('onda4')

window.addEventListener('scroll', function(){
    var rolagemPos = window.scrollY

    onda1.style.backgroundPositionX = 500 + rolagemPos * 4 + 'px';
    onda2.style.backgroundPositionX = 400 + rolagemPos * -4 + 'px';
    onda3.style.backgroundPositionX = 300 + rolagemPos * 2 + 'px';
})
