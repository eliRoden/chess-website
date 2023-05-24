 
function print(boardString) {

  let boardArr = [];
  for (let i = 0; i < 8; i++) {
    let row = []
    for (let j = 0; j < 8; j++) {
      row.push(" ");
    }
    boardArr.push(row);
  }
  for (let k = 0; k < 64; k++) {
    boardArr[Math.floor(k/8)][k%8] = boardString[k];
  }
  const table = document.getElementById('chessboard');
  while (table.rows.length > 0) {
    table.deleteRow(0);
  }

  const row = table.insertRow(0);
  let emptyCell = row.insertCell(0);
  let clickCount = 0;
  
  for (let l = 1; l < 9; l++) {
    let cell = row.insertCell(l);
    let letter = document.createTextNode(String.fromCharCode(l+64));
    cell.appendChild(letter);
    cell.setAttribute("class","topRow");
  }
  for (let i = 0; i < 8; i++) {
    const row = document.createElement('tr');
    let newCell = row.insertCell(0);
    let text = document.createTextNode(i);
    newCell.appendChild(text);
    for (let j = 0; j < 8; j++) {
      const cell = document.createElement('td');
      if ((i + j) % 2 === 0) {
        cell.classList.add('white');
      } else {
        cell.classList.add('black');
      }
      if (boardArr[i][j] != " ") {
        const img = document.createElement('img');
        img.classList.add('piece');
        if (boardArr[i][j] === "p") {
          img.src = imageUrls.whitePawn;
        } else if (boardArr[i][j] === "P") {
          img.src = imageUrls.blackPawn;
        } else if (boardArr[i][j] === "r") {
          img.src = imageUrls.whiteRook;
        } else if (boardArr[i][j] === "R") {
          img.src = imageUrls.blackRook;
        } else if (boardArr[i][j] === "n") {
          img.src = imageUrls.whiteKnight;
        } else if (boardArr[i][j] === "N") {
          img.src = imageUrls.blackKnight;
        } else if (boardArr[i][j] === "b") {
          img.src = imageUrls.whiteBishop;
        } else if (boardArr[i][j] === "B") {
          img.src = imageUrls.blackBishop;
        } else if (boardArr[i][j] === "q") {
          img.src = imageUrls.whiteQueen;
        } else if (boardArr[i][j] === "Q") {
          img.src = imageUrls.blackQueen;
        } else if (boardArr[i][j] === "k") {
          img.src = imageUrls.whiteKing;
        } else if (boardArr[i][j] === "K") {
          img.src = imageUrls.blackKing;
        }
        cell.appendChild(img);
      }        

      var pieceI;
      var pieceJ;
      cell.setAttribute("id",i+" "+j);
      cell.addEventListener("click", e => {
          if (clickCount === 0) {
            pieceI = i;
            pieceJ = j;
            clickCount++;
            cell.classList.add("highlight");
          }
          else if (clickCount === 1) {
              let x = e.clientX;
              let y = e.clientY;
              
              for (let l = 0; l < 8; l++) {
                for (let m = 0; m < 8; m++) {
                  let c = document.getElementById(l+" "+m);
                  if (c) {
                    let cBound = c.getBoundingClientRect();

                    if (x >= cBound.left && x <= cBound.right && y >= cBound.top && y <= cBound.bottom) {
                      window.location.href = '/move/' + pieceI+pieceJ+l+m;
                      //moveRequest( pieceI, pieceJ, l, m);
                      document.getElementById(pieceI+" "+pieceJ).classList.remove("highlight");
                      break;
                    }
                  }
                  
                }
              }
              clickCount = 0;
          }
        });
      row.appendChild(cell);
    }
    table.appendChild(row);
  }

  let whiteScoreDif, blackScoreDif
  if (this.whiteScore > this.blackScore) {
    whiteScoreDif = "+" + String(this.whiteScore - this.blackScore);
    blackScoreDif = "";
  } else if (this.blackScore > this.whiteScore) {
    blackScoreDif = "+" + String(this.blackScore - this.whiteScore);
    whiteScoreDif = "";
  } else {
    whiteScoreDif = "";
    blackScoreDif = "";
  }
  console.log(whiteScoreDif + " " + blackScoreDif);
  const scoreTable = document.getElementById("score");
  const scoreRow = scoreTable.insertRow();
  let scoreCell = scoreRow.insertCell();
  let score = document.createTextNode(whiteScoreDif+" "+blackScoreDif);
  scoreCell.appendChild(score);
}

print(board);

if (checkmate) {
  if (whites_turn) {
    alert("White is in checkmate,\nBlack wins!");
  } else {
    alert("Black is in checkmate,\nWhite wins!");
  }
}
