// 0. return empty array if input is not a string
// 1. for loop which goes maximum by 8 squares in every chessboard direction
// 2. track every direction movement (8 different directions)
// 3. make sure that every direction doesn't cross the border like A-H or 1-8
// 4. add possible squares on every iteration from every direction, so you will add maximum of 8 possible squares on every iteration
// 5. return sorted array of possible squares

function availableMoves(position) {
  if (typeof position !== 'string' || position.length !== 2) return []

  const [posCol, posRow] = position.split('')

  if (
    posCol.charCodeAt(0) < 65 ||
    posCol.charCodeAt(0) > 72 ||
    parseInt(posRow) < 1 ||
    parseInt(posRow) > 8
  ) {
    return []
  }

  const queenColPos = posCol.charCodeAt(0) // ascii number
  const queenRowPos = +posRow // number

  let directions = {
    up: null,
    down: null,
    left: null,
    right: null,
  }

  const results = []

  for (let i = 1; i < 8; i++) {
    // moving up
    if (queenRowPos + i <= 8) {
      directions = {
        ...directions,
        up: queenRowPos + i,
      }

      results.push(posCol + directions.up)
    }

    // moving down
    if (queenRowPos - i >= 1) {
      directions = {
        ...directions,
        down: queenRowPos - i,
      }
      results.push(posCol + directions.down)
    }

    // moving left
    if (queenColPos - i >= 65) {
      directions = {
        ...directions,
        left: queenColPos - i,
      }
      results.push(String.fromCharCode(directions.left) + posRow)
    }

    // moving right
    if (queenColPos + i <= 72) {
      directions = {
        ...directions,
        right: queenColPos + i,
      }
      results.push(String.fromCharCode(directions.right) + posRow)
    }

    // moving left and up
    if (queenColPos - i >= 65 && queenRowPos + i <= 8) {
      results.push(String.fromCharCode(directions.left) + directions.up)
    }

    // moving right and up
    if (queenColPos + i <= 72 && queenRowPos + i <= 8) {
      results.push(String.fromCharCode(directions.right) + directions.up)
    }

    // moving left and down
    if (queenColPos - i >= 65 && queenRowPos - i >= 1) {
      results.push(String.fromCharCode(directions.left) + directions.down)
    }

    // moving right and down
    if (queenColPos + i <= 72 && queenRowPos - i >= 1) {
      results.push(String.fromCharCode(directions.right) + directions.down)
    }
  }
  return results.sort()
}

const tests = [
  {
    input: 'A1',
    expected: [
      'A2',
      'A3',
      'A4',
      'A5',
      'A6',
      'A7',
      'A8',
      'B1',
      'B2',
      'C1',
      'C3',
      'D1',
      'D4',
      'E1',
      'E5',
      'F1',
      'F6',
      'G1',
      'G7',
      'H1',
      'H8',
    ],
  },
  {
    input: 'C5',
    expected: [
      'A3',
      'A5',
      'A7',
      'B4',
      'B5',
      'B6',
      'C1',
      'C2',
      'C3',
      'C4',
      'C6',
      'C7',
      'C8',
      'D4',
      'D5',
      'D6',
      'E3',
      'E5',
      'E7',
      'F2',
      'F5',
      'F8',
      'G1',
      'G5',
      'H5',
    ],
  },
  {
    input: 'H3',
    expected: [
      'A3',
      'B3',
      'C3',
      'C8',
      'D3',
      'D7',
      'E3',
      'E6',
      'F1',
      'F3',
      'F5',
      'G2',
      'G3',
      'G4',
      'H1',
      'H2',
      'H4',
      'H5',
      'H6',
      'H7',
      'H8',
    ],
  },
  {
    input: null,
    expected: [],
  },
  {
    input: [1, 2, 3],
    expected: [],
  },
  {
    input: 'work?',
    expected: [],
  },
  {
    input: 'A10',
    expected: [],
  },
  {
    input: 'B0',
    expected: [],
  },
  {
    input: 2,
    expected: [],
  },
]

for (let i in tests) {
  let result = availableMoves(tests[i]['input'])
  if (!Array.isArray(result)) {
    console.error('Result should be an array.')
  }
  console.log(result, tests[i]['expected'])
}
