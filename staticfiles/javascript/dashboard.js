const newAnimalButton = document.querySelector("#new-animal-button")
const AnimalInputForm = document.querySelector("#animal-input-form")
const AnimalCloseForm = document.querySelector("#animal-close-button")
const bigNum = document.getElementsByClassName("big-number")
const topBox = document.getElementsByClassName("top-box")


newAnimalButton.addEventListener( "click", () => {
    AnimalInputForm.style.display = "block";
})

AnimalCloseForm.addEventListener("click", () => {
    AnimalInputForm.style.display = "none";
})


for (let i = 0; i < topBox.length; i++) {
    const BigNum = topBox[i].getElementsByClassName("big-number")
    if (bigNum.offsetWidth > topBox[i].offsetWidth) {
        console.log('howdy');
    }
    console.log('pig');
}