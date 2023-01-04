const mainCont = document.getElementsByClassName("triangle-container")
const animalImage = document.querySelector("#chicken-img")

const blue = '#6977E6'
for (let i = 0; i < mainCont.length; i++) {
    mainCont[i].addEventListener('mouseenter', () => {
        mainCont[i].querySelector(".forum-text").classList.add("shaking-animation");
        mainCont[i].style.backgroundColor = "white";
        const leftTriangle = mainCont[i].querySelector(".left-triangle")
        const rightTriangle = mainCont[i].querySelector(".right-triangle")
        leftTriangle.classList.add("forum-onclick-animation-left")
        rightTriangle.classList.add("forum-onclick-animation-right")
        leftTriangle.style.transform = "scale(0.5)";
        rightTriangle.style.transform = "scale(0.5)";
    })
    mainCont[i].addEventListener('mouseleave', () => {
        mainCont[i].querySelector(".forum-text").classList.remove("shaking-animation");
        mainCont[i].style.backgroundColor = "white";
        const leftTriangle = mainCont[i].querySelector(".left-triangle")
        const rightTriangle = mainCont[i].querySelector(".right-triangle")
        leftTriangle.classList.remove("forum-onclick-animation-left")
        rightTriangle.classList.remove("forum-onclick-animation-right")
        mainCont[i].style.backgroundColor = blue;
    })
    mainCont[i].addEventListener("click", () => {
        const animal =mainCont[i].querySelector(".forum-text");
        leadToRoom(animal)
    })
}



function leadToRoom(roomname) {
    var roomName = roomname.textContent;
    window.location.pathname = '/' + "chat" + "/" + roomName + '/';
};

