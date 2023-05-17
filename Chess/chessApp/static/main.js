const PieceColor = {
  white: 0,
  black: 1
};

const Pieces = {
  pawn: 0,
  rook: 1,
  knight: 2,
  bishop: 3,
  queen: 4,
  king: 5
}

class Piece {
  constructor(color, type, i, j, value) {
    this.color = color;
    this.type = type;
    this.i = i;
    this.j = j;
    this.value = value;
  }

  canTake(otherPiece) { return this.color != otherPiece.color; }

  move(i, j) {
    this.i = i;
    this.j = j;
  }

  toString() {
    let toRet = "";

    if (this.color === PieceColor.white) toRet += "W";
    else toRet += "B";

    if (this.type === Pieces.pawn) toRet += "P";
    if (this.type === Pieces.rook) toRet += "R";
    if (this.type === Pieces.knight) toRet += "k";
    if (this.type === Pieces.bishop) toRet += "B";
    if (this.type === Pieces.queen) toRet += "Q";
    if (this.type === Pieces.king) toRet += "K";

    return toRet;
  }
}

class King extends Piece {
  constructor(color, i, j) { super(color, Pieces.king, i, j, 0); }
  
  isValidMove(x, y) { return x >= this.i - 1 && x <= this.i + 1 && y >= this.j -1 && y <= this.j + 1; }
}

class Knight extends Piece {

  constructor(color,  i,  j) { super(color, Pieces.knight, i, j, 3); }
  
  isValidMove(x, y) {
    if (x === this.i + 2 && y === this.j + 1) return true;
    if (x === this.i + 1 && y === this.j + 2) return true;
    if (x === this.i - 2 && y === this.j + 1) return true;
    if (x === this.i - 1 && y === this.j + 2) return true;
    if (x === this.i + 2 && y === this.j - 1) return true;
    if (x === this.i + 1 && y === this.j - 2) return true;
    if (x === this.i - 2 && y === this.j - 1) return true;
    if (x === this.i - 1 && y === this.j - 2) return true;
    
    return false;
  }
}

class Queen extends Piece {

  constructor(color, i, j) { super(color, Pieces.queen, i, j, 9); }

  isValidMove(x, y) {
    for (let n = 1; n < 8; n++) {
      if (x === this.i + n && y === this.j + n) return true;
      if (x === this.i - n && y === this.j + n) return true;
      if (x === this.i + n && y === this.j - n) return true;
      if (x === this.i - n && y === this.j - n) return true;
    }
    
    return x === this.i || y === this.j;
  }
}

class Bishop extends Piece {

  constructor(color, i, j) { super(color, Pieces.bishop, i, j, 3); }
  
  isValidMove(x, y) {
    for (let n = 1; n < 8; n++) {
      if (x === this.i + n && y === this.j + n) return true;
      if (x === this.i - n && y === this.j + n) return true;
      if (x === this.i + n && y === this.j - n) return true;
      if (x === this.i - n && y === this.j - n) return true;
    }
    
    return false;
  }
}

class Rook extends Piece {

  constructor(color, i, j) { super(color, Pieces.rook, i, j, 5); }
  
  isValidMove(x, y) {
    return x === this.i || y === this.j;
  }
}

class Pawn extends Piece {

  constructor(color, i, j) { super(color, Pieces.pawn, i, j, 1); }
//3,4 --> 4,5
  isValidMove(x, y) {
    if (this.color === PieceColor.white) {
      if (y === this.j && x === this.i - 1) return true;
      if (y === this.j - 1 && x === this.i - 1) return true;
      if (y === this.j + 1 && x === this.i - 1) return true;
      if (this.i === 6 && x === 4 && y === this.j) return true;
    }

    if (this.color === PieceColor.black) {
      if (y === this.j && x === this.i + 1) return true;
      if (y === this.j + 1 && x === this.i + 1) return true;
      if (y === this.j - 1 && x === this.i + 1) return true;
      if (this.i === 1 && x === 3 && y === this.j) return true;
    }

    return false;
  }
}

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
    this.inGame = true;
    this.turn = PieceColor.white;
    this.whiteKingMoved = false;
    this.leftWhiteRookMoved = false;
    this.rightWhiteRookMoved = false;
    this.blackKingMoved = false;
    this.leftBlackRookMoved = false;
    this.rightBlackRookMoved = false;
    this.whiteScore = 0;
    this.blackScore = 0;

    for (let j = 0; j < 8; j++) {
      this.board[1][j] = new Pawn(PieceColor.black, 1, j);
      this.board[6][j] = new Pawn(PieceColor.white, 6, j);
      switch (j) {
        case 0:
        case 7:
          this.board[0][j] = new Rook(PieceColor.black, 0, j);
          this.board[7][j] = new Rook(PieceColor.white, 7, j);
          break;
        case 1:
        case 6:
          this.board[0][j] = new Knight(PieceColor.black, 0, j);
          this.board[7][j] = new Knight(PieceColor.white, 7, j);
          break;
        case 2:
        case 5:
          this.board[0][j] = new Bishop(PieceColor.black, 0, j);
          this.board[7][j] = new Bishop(PieceColor.white, 7, j);
          break;
        case 3:
          this.board[0][j] = new Queen(PieceColor.black, 0, j);
          this.board[7][j] = new Queen(PieceColor.white, 7, j);
          break;
        case 4:
          this.board[0][j] = new King(PieceColor.black, 0, j);
          this.board[7][j] = new King(PieceColor.white, 7, j);
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
          if (this.board[i][j].color === PieceColor.white && this.board[i][j].type === Pieces.pawn) {
            img.src = imageUrls.whitePawn;
          } else if (this.board[i][j].color === PieceColor.black && this.board[i][j].type === Pieces.pawn) {
            img.src = imageUrls.blackPawn;
          } else if (this.board[i][j].color === PieceColor.white && this.board[i][j].type === Pieces.rook) {
            img.src = imageUrls.whiteRook;
          } else if (this.board[i][j].color === PieceColor.black && this.board[i][j].type === Pieces.rook) {
            img.src = imageUrls.blackRook;
          } else if (this.board[i][j].color === PieceColor.white && this.board[i][j].type === Pieces.knight) {
            img.src = imageUrls.whiteKnight;
          } else if (this.board[i][j].color === PieceColor.black && this.board[i][j].type === Pieces.knight) {
            img.src = imageUrls.blackKnight;
          } else if (this.board[i][j].color === PieceColor.white && this.board[i][j].type === Pieces.bishop) {
            img.src = imageUrls.whiteBishop;
          } else if (this.board[i][j].color === PieceColor.black && this.board[i][j].type === Pieces.bishop) {
            img.src = imageUrls.blackBishop;
          } else if (this.board[i][j].color === PieceColor.white && this.board[i][j].type === Pieces.queen) {
            img.src = imageUrls.whiteQueen;
          } else if (this.board[i][j].color === PieceColor.black && this.board[i][j].type === Pieces.queen) {
            img.src = imageUrls.blackQueen;
          } else if (this.board[i][j].color === PieceColor.white && this.board[i][j].type === Pieces.king) {
            img.src = imageUrls.whiteKing;
          } else if (this.board[i][j].color === PieceColor.black && this.board[i][j].type === Pieces.king) {
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

//                 3, 4, 4, 5
  movePiece(piece, i, j, x, y) {
    let pieceCaptured = this.board[x][y];
    if (pieceCaptured != null && pieceCaptured.color === PieceColor.black) this.whiteScore += pieceCaptured.value;
    if (pieceCaptured != null && pieceCaptured.color === PieceColor.white) this.blackScore += pieceCaptured.value;
    piece.move(x, y);
    this.board[x][y] = piece;
    this.board[i][j] = null;
    if (piece.type === Pieces.king && piece.color === PieceColor.white) this.whiteKingMoved = true;
    if (piece.type === Pieces.king && piece.color === PieceColor.black) this.blackKingMoved = true;
    if (piece.type === Pieces.rook && piece.color === PieceColor.white && i === 7 && j === 0) this.leftWhiteRookMoved = true;
    if (piece.type === Pieces.rook && piece.color === PieceColor.black && i === 7 && j === 0) this.leftBlackRookMoved = true;
    if (piece.type === Pieces.rook && piece.color === PieceColor.white && i === 0 && j === 7) this.rightWhiteRookMoved = true;
    if (piece.type === Pieces.rook && piece.color === PieceColor.black && i === 0 && j === 7) this.rightBlackRookMoved = true;
  }
  
  isValidMove(i, j, x, y) {
    if (i < 0 || j < 0 || x < 0 || y < 0 || i > 7 || j > 7 || x > 7 || y > 7 ) {
      return false;
    }

    if (i === x && j === y) return false;

    let piece = this.board[i][j];
    
    if (piece === null) return false;

    if (this.board[x][y] != null && !piece.canTake(this.board[x][y])) return false;

    if (piece.type === Pieces.pawn && j != y && this.board[x][y] === null) return false;

    if (!piece.isValidMove(x, y)) return false;

    return true;
  }

  canCastle(castlingLeft) {
    if (this.inCheck(this.turn)) return false;

    if (this.turn === PieceColor.white && castlingLeft === true) {
      if (this.whiteKingMoved || this.leftWhiteRookMoved) return false;
      for (let j = 1; j < 4; j++) {
        if (this.board[7][j] != null) return false;
      }
    } else if (this.turn === PieceColor.white && castlingLeft === false) {
      if (this.whiteKingMoved || this.rightWhiteRookMoved) return false;
      for (let j = 6; j > 4; j--) {
        if (this.board[7][j] != null) return false;
      }
    } else if (this.turn === PieceColor.black && castlingLeft === true) {
      if (this.blackKingMoved || this.leftBlackRookMoved) return false;
      for (let j = 1; j < 4; j++) {
        if (this.board[0][j] != null) return false;
      }
    } else if (this.turn === PieceColor.black && castlingLeft === false) {
      if (this.blackKingMoved || this.rightBlackRookMoved) return false;
      for (let j = 6; j > 4; j--) {
        if (this.board[7][j] != null) return false;
      }
    }

    return true;
  }

  castle(color, castlingLeft) {
    if (color === PieceColor.white && castlingLeft === true) {
      this.movePiece(this.board[7][4], 7, 4, 7, 2);
      this.movePiece(this.board[7][0], 7, 0, 7, 3);
    } else if (color === PieceColor.white && castlingLeft === false) {
      this.movePiece(this.board[7][4], 7, 4, 7, 6);
      this.movePiece(this.board[7][7], 7, 7, 7, 5);
    } else if (color === PieceColor.black && castlingLeft === true) {
      this.movePiece(this.board[0][4], 0, 4, 0, 2);
      this.movePiece(this.board[0][0], 0, 0, 0, 3);
    } else if (color === PieceColor.black && castlingLeft === false) {
      this.movePiece(this.board[0][4], 0, 4, 0, 6);
      this.movePiece(this.board[0][7], 0, 7, 0, 5);
    }
  }

  canEnPassant(i,j,passingLeft) {
    if (this.turn === PieceColor.white && passingLeft === true) {
      if (this.board[i][j-1] != null && this.board[i][j-1].type === Pieces.pawn && this.board[i][j-1].color === PieceColor.black) {
        if (this.board[i-1][j-1] === null) return true;
      }
    } else if (this.turn === PieceColor.white && passingLeft === false) {
      if (this.board[i][j+1] != null && this.board[i][j+1].type === Pieces.pawn && this.board[i][j+1].color === PieceColor.black) {
        if (this.board[i-1][j+1] === null) return true;
      }
    } else if (this.turn === PieceColor.black && passingLeft === true) {
      if (this.board[i][j-1] != null && this.board[i][j-1].type === Pieces.pawn && this.board[i][j-1].color === PieceColor.white) {
        if (this.board[i+1][j-1] === null) return true;
      }
    } else if (this.turn === PieceColor.black && passingLeft === false) {
      if (this.board[i][j+1] != null && this.board[i][j+1].type === Pieces.pawn && this.board[i][j+1].color === PieceColor.white) {
        if (this.board[i+1][j+1] === null) return true;
      }
    }
    return false;
  }
  

  enPassant(color,passingLeft,j) {
    if (color === PieceColor.white && passingLeft === true) {
      this.movePiece(this.board[3][j],3,j,2,j-1);
      this.board[3][j-1] = null;
      this.whiteScore++;
    } else if (color === PieceColor.white && passingLeft === false) {
      this.movePiece(this.board[3][j],3,j,2,j+1);
      this.board[3][j+1] = null;
      this.whiteScore++;
    } else if (color === PieceColor.black && passingLeft === true) {
      this.movePiece(this.board[4][j],4,j,5,j-1);
      this.board[4][j-1] = null;
      this.blackScore++;
    } else if (color === PieceColor.black && passingLeft === false) {
      this.movePiece(this.board[4][j],4,j,5,j+1);
      this.board[4][j+1] = null;
      this.blackScore++;
    }
  }

  inCheck(color) {
    let ki = 0, kj = 0;
    for (let i = 0; i < this.board.length; i++) {
      for (let j = 0; j < this.board[i].length; j++) {
        if (this.board[i][j] != null && this.board[i][j].color === color && this.board[i][j].type === Pieces.king) {
          ki = i;
          kj = j;
        }
      }
    }
    
    for (let i = 0; i < this.board.length; i++) {
      for (let j = 0; j < this.board[i].length; j++) {
        if (this.isValidMove(i,j,ki,kj)) {
          let p = this.board[i][j];
          if (p.type === Pieces.knight) {
            return true;
          } else if (p.type === Pieces.pawn) {
            return true;
          } else if (p.type === Pieces.bishop) {
            let kingProtected = false;
            
            if (i < ki && j < kj) {
              for (let d = 1; d < ki - i; d++) {
                if (i + d > 7 || j + d > 7) break;
                if (this.board[i + d][j + d] != null) kingProtected = true;
              }
            }
            
            if (i > ki && j < kj) {
              for (let d = 1; d < i - ki; d++) {
                if (i - d < 0 || j + d > 7) break;
                if (this.board[i - d][j + d] != null) kingProtected = true;
              }
            }
            
            if (i < ki && j > kj) {
              for (let d = 1; d < ki - i; d++) {
                if (i + d < 0 || j - d > 7) break;
                if (this.board[i + d][j - d] != null) kingProtected = true;
              }
            }
            
            if (i > ki && j > kj) {
              for (let d = 1; d < i - ki; d++) {
                if (i - d < 0 || j - d < 0) break;
                if (board[i - d][j - d] != null) kingProtected = true;
              }
            }
            
            if (!kingProtected) return true;
          } else if (p.type === Pieces.rook) {
            let kingProtected = false;
            
            if (i < ki && j === kj) {
              for (let d = 1; d < ki - i; d++) {
                if (i + d > 7) break;
                if (this.board[i + d][j] != null) kingProtected = true;
              }
            }
            
            if (i > ki && j === kj) {
              for (let d = 1; d < i - ki; d++) {
                if (i - d < 0) break;
                if (this.board[i - d][j] != null) kingProtected = true;
              }
            }
            
            if (i === ki && j < kj) {
              for (let d = 1; d < kj - j; d++) {
                if (j + d > 7) break;
                if (this.board[i][j + d] != null) kingProtected = true;
              }
            }
            
            if (i === ki && j > kj) {
              for (let d = 1; d < j - kj; d++) {
                if (j - d < 0) break;
                if (this.board[i][j - d] != null) kingProtected = true;
              }
            }
            
            if (!kingProtected) return true;
          } else if (p.type === Pieces.queen) {
            let kingProtected = false;
            
            if (i < ki && j < kj) {
              for (let d = 1; d < ki - i; d++) {
                if (i + d > 7 || j + d > 7) break;
                if (this.board[i + d][j + d] != null) kingProtected = true;
              }
            }
            
            if (i > ki && j < kj) {
              for (let d = 1; d < i - ki; d++) {
                if (i - d < 0 || j + d > 7) break;
                if (this.board[i - d][j + d] != null) kingProtected = true;
              }
            }
            
            if (i < ki && j > kj) {
              for (let d = 1; d < ki - i; d++) {
                if (i + d < 0 || j - d > 7) break;
                if (this.board[i + d][j - d] != null) kingProtected = true;
              }
            }
            
            if (i > ki && j > kj) {
              for (let d = 1; d < i - ki; d++) {
                if (i - d < 0 || j - d < 0) break;
                if (this.board[i - d][j - d] != null) kingProtected = true;
              }
            }
            
            if (i < ki && j === kj) {
              for (let d = 1; d < ki - i; d++) {
                if (i + d > 7) break;
                if (this.board[i + d][j] != null) kingProtected = true;
              }
            }
            
            if (i > ki && j === kj) {
              for (let d = 1; d < i - ki; d++) {
                if (i - d < 0) break;
                if (this.board[i - d][j] != null) kingProtected = true;
              }
            }
            
            if (i === ki && j < kj) {
              for (let d = 1; d < kj - j; d++) {
                if (j + d > 7) break;
                if (this.board[i][j + d] != null) kingProtected = true;
              }
            }
            
            if (i === ki && j > kj) {
              for (let d = 1; d < j - kj; d++) {
                if (j - d < 0) break;
                if (this.board[i][j - d] != null) kingProtected = true;
              }
            }
            
            if (!kingProtected) return true;
          }   
        }
      }
    }

    return false;
  }
  
  checkMate(color) {
    if (!this.inCheck(color)) return false;

    let ki = 0, kj = 0;
    for (let i = 0; i < this.board.length; i++) {
      for (let j = 0; j < this.board[i].length; j++) {
        let p = this.board[i][j]
        if (p != null && p.color === color && p.type === Pieces.king) {
          ki = i;
          kj = j;
	      }
      }
    }

    for (let i = ki - 1; i <= ki + 1; i++) {
      for (let j = kj - 1; j <= kj + 1; j++) {
	      if (this.isValidMove(ki, kj, i, j) && this.isValidCheck(ki, kj, i, j)) return false;
      }
    }

    return true;
  }
  
  isValidCheck(i, j, x, y) {
    this.movePiece(this.board[i][j], i, j, x, y);
    if (this.inCheck(this.turn)) {
      this.movePiece(this.board[x][y], x, y, i, j);
      return false;
    } else {
      this.movePiece(this.board[x][y], x, y, i, j);
      return true;
    }
  }
}

function clearText() {
   document.getElementById("move").value=""; 
}


var game = new Game();
game.print();
//                   3, 4, 4, 5
function moveRequest(i, j, x, y) {
  /*
  move = document.getElementById("move").value;
  current = move.substring(0,2);
  newPos = move.substring(move.length - 2);

  let i = Number(current.charAt(1));
  let j = current.charAt(0).charCodeAt(0) - 97;
  let x = Number(newPos.charAt(1));
  let y = newPos.charAt(0).charCodeAt(0) - 97;
  */
 
  if (i === 7 && j === 4 && x === 7 && y === 2 && game.canCastle(true)) {
    game.castle(game.turn, true);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 7 && j === 4 && x === 7 && y === 6 && game.canCastle(false)) {
    game.castle(game.turn, false);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 0 && j === 4 && x === 0 && y === 2 && game.canCastle(true)) {
    game.castle(game.turn, true);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 0 && j === 4 && x === 0 && y === 6 && game.canCastle(false)) {
    game.castle(game.turn, false);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 3 && x === 2 && y === j-1 && game.canEnPassant(i,j,true)) {
    game.enPassant(game.turn,true,j);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 3 && x === 2 && y === j+1 && game.canEnPassant(i,j,false)) {
    game.enPassant(game.turn,false,j);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 4 && x === 5 && y === j-1 && game.canEnPassant(i,j,true)) {
    game.enPassant(game.turn,true,j);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (i === 4 && x === 5 && y === j+1 && game.canEnPassant(i,j,false)) {
    game.enPassant(game.turn,false,j);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else if (game.isValidMove(i, j, x, y) && game.isValidCheck(i, j, x, y) && game.board[i][j].color === game.turn) {
    game.movePiece(game.board[i][j], i, j, x, y);
    game.print();
    if (game.turn === PieceColor.white) game.turn = PieceColor.black;
    else game.turn = PieceColor.white;
  } else {
    console.log("isValidMove: "+game.isValidMove(i,j,x,y));
    console.log("turn" + game.turn);
    alert("Invalid move");
  }

  if (game.checkMate(PieceColor.white)) {
    alert("Black wins");
    game.inGame = false;
  } 

  if (game.checkMate(PieceColor.black)) {
    alert("White wins");
    game.inGame = false;
  }
  
}
