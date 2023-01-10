const newAnimalButton = document.querySelector("#new-animal-button")
const AnimalInputForm = document.querySelector("#animal-input-form")
const AnimalCloseForm = document.querySelector("#animal-close-button")

newAnimalButton.addEventListener( "click", () => {
    AnimalInputForm.style.display = "block";
})

AnimalCloseForm.addEventListener("click", () => {
    AnimalInputForm.style.display = "none";
})