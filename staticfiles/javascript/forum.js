const mainCont = document.getElementsByClassName("triangle-container")


const blue = '#37408b'
const pink = "#F4ABC4"
const red = "#F30A49"
for (let i = 0; i < mainCont.length; i++) {
    mainCont[i].addEventListener('mouseenter', () => {
        const text = mainCont[i].querySelector(".forum-text")
        text.classList.add("shaking-animation");
        text.style.color = red
        mainCont[i].querySelector(".animal-img").classList.add("shaking-animation");
        mainCont[i].style.backgroundColor = pink;
        const leftTriangle = mainCont[i].querySelector(".left-triangle")
        const rightTriangle = mainCont[i].querySelector(".right-triangle")
        leftTriangle.classList.add("forum-onclick-animation-left")
        rightTriangle.classList.add("forum-onclick-animation-right")
        leftTriangle.style.transform = "scale(0.5)";
        rightTriangle.style.transform = "scale(0.5)";
    })
    mainCont[i].addEventListener('mouseleave', () => {
        const text = mainCont[i].querySelector(".forum-text")
        text.classList.remove("shaking-animation");
        text.style.color = "white"
        mainCont[i].querySelector(".animal-img").classList.remove("shaking-animation");
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

