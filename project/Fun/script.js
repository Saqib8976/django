console.log("Welcome to Tic Tac Toa")
let music = new Audio('gameon.mp3')
let audioTurn = new Audio('ting.mp3')
let gameover = new Audio('GameOver.mp3')

let turnX = true;


const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
]

let btns = document.querySelectorAll(".btn");
let resetbtn = document.querySelector("#reset");

btns.forEach((btn) => {
    btn.addEventListener('click', () => {
        console.log("box is clicked")


        if (turnX === true) {

            btn.innerText = "X";
            turnX = false;
        }
        else {

            btn.innerText = "O";
            turnX = true;
        }
        btn.disabled = true;

    })
});

const checkwinner = () => {
    for (let pattern of winPatterns) {

        let pos1Val = btns[pattern[0]].innerText;
        let pos2Val = btns[pattern[1]].innerText;
        let pos3Val = btns[pattern[2]].innerText;

        if (pos1Val != "" && pos2Val != "" && pos3Val != "") {
            if (pos1Val === pos2Val && pos2Val === pos3Val) {
                console.log("winner...")
            }
        }

    }
};









//function to check win
// const checkWin = () => {

// }

//game logic

// let boxes = document.getElementsByClassName("box");
// Array.from(boxes).forEach(element => {
//     let boxtext = element.querySelector('.boxtext');

//     element.addEventListener('click', () => {

//         if (boxtext.innertext === '') {
//             boxtext.innertext = turn;
//             turn = changeTurn();
//             audioTurn.play();
//             // checkWin();
//             document.getElementsByClassName("info")[0].innertext = "Turn for " + turn;
//             console.log("check")
//         }
//     })
// })