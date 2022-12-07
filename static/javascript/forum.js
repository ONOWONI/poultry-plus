const chicken = document.querySelector('#chicken');
const turkey =document.querySelector('#turkey');
const fish = document.querySelector('#fish');
const sheep = document.querySelector('#sheep');
const goat = document.querySelector('#goat');
const cow = document.querySelector('#cow');


// document.querySelector('#room-name-input').focus();

// document.querySelector('#room-name-input').onkeyup = function(e) {
//     if (e.keyCode === 13) {  // enter, return
//         document.querySelector('#room-name-submit').click();
// }
// };

// document.querySelector('#room-name-submit').onclick = function(e) {
//     var roomName = document.querySelector('#room-name-input').value;
//     window.location.pathname = '/chat/' + roomName + '/';
// };



chicken.addEventListener("click", () => {
    leadToRoom(chicken)
} )
turkey.addEventListener("click", () => {
    leadToRoom(turkey)
} )
fish.addEventListener("click", () => {
    leadToRoom(fish)
} )
sheep.addEventListener("click", () => {
    leadToRoom(sheep)
} )
goat.addEventListener("click", () => {
    leadToRoom(goat)
} )
cow.addEventListener("click", () => {
    leadToRoom(cow)
} )
// fish.onclick(leadToRoom(fish))
// sheep.onclick(leadToRoom(sheep))
// goat.onclick(leadToRoom(goat))
// cow.onclick(leadToRoom(cow))

function leadToRoom(roomname) {
    var roomName = roomname.textContent;
    window.location.pathname = '/' + "chat" + "/" + roomName + '/';
};

