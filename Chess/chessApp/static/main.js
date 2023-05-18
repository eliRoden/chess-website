class Game {
  constructor() {
    this.board = [];
    for (let i = 0; i < 8; i++) {
      let row = []
      for (let j = 0; j < 8; j++) {
        row.push(null);
      }
      this.board.push(row);
    }

    for (let j = 0; j < 8; j++) {
      this.board[1][j] = "P";
      this.board[6][j] = "p";
      switch (j) {
        case 0:
        case 7:
          this.board[0][j] = "R";
          this.board[7][j] = "r";
          break;
        case 1:
        case 6:
          this.board[0][j] = "N";
          this.board[7][j] = "n";
          break;
        case 2:
        case 5:
          this.board[0][j] = "B";
          this.board[7][j] = "b";
          break;
        case 3:
          this.board[0][j] = "Q";
          this.board[7][j] = "q";
          break;
        case 4:
          this.board[0][j] = "K";
          this.board[7][j] = "k";
          break;
      }
    }
  }
  
  print() {
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
				if (this.board[i][j] != null) {
          const img = document.createElement('img');
          img.classList.add('piece');
          if (this.board[i][j] === "p") {
            img.src = imageUrls.whitePawn;
          } else if (this.board[i][j] === "P") {
            img.src = imageUrls.blackPawn;
          } else if (this.board[i][j] === "r") {
            img.src = imageUrls.whiteRook;
          } else if (this.board[i][j] === "R") {
            img.src = imageUrls.blackRook;
          } else if (this.board[i][j] === "n") {
            img.src = imageUrls.whiteKnight;
          } else if (this.board[i][j] === "N") {
            img.src = imageUrls.blackKnight;
          } else if (this.board[i][j] === "b") {
            img.src = imageUrls.whiteBishop;
          } else if (this.board[i][j] === "B") {
            img.src = imageUrls.blackBishop;
          } else if (this.board[i][j] === "q") {
            img.src = imageUrls.whiteQueen;
          } else if (this.board[i][j] === "Q") {
            img.src = imageUrls.blackQueen;
          } else if (this.board[i][j] === "k") {
            img.src = imageUrls.whiteKing;
          } else if (this.board[i][j] === "K") {
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
                        moveRequest( pieceI, pieceJ, l, m);
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
}


var game = new Game();
game.print();
