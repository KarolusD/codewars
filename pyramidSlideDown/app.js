function longestSlideDown(pyramid) {
  let currIdx = 0
  let sum = pyramid[0][0]
  for (let i = 1; i < pyramid.length; i++) {
    if (pyramid[i][currIdx] > pyramid[i][currIdx + 1]) {
      currIdx = pyramid[i].indexOf(pyramid[i][currIdx])
    } else {
      currIdx = pyramid[i].indexOf(pyramid[i][currIdx + 1])
    }
    console.log('current element -->> ', pyramid[i][currIdx])

    let potentialBiggerSlideDown = lookingForBiggerSlideDown(
      pyramid.slice(0, i + 1),
      pyramid[i],
      pyramid[i][currIdx]
    )
    sum += pyramid[i][currIdx]
    if (
      potentialBiggerSlideDown !== null &&
      potentialBiggerSlideDown.sum > sum
    ) {
      old = sum
      sum = potentialBiggerSlideDown.sum
      currIdx = potentialBiggerSlideDown.idx
      console.log(old, '-->', sum, 'sum changed!')
      //if (i !== pyramid.length - 1) i++
      console.log('current element -->> ', pyramid[i][currIdx])
    }
    console.log(sum, '<<-- current sum')
  }
  console.log('FINAL ANS: ', sum)
}

function lookingForBiggerSlideDown(pyramid, currRow, currNum) {
  let biggerNumIdx = null
  let slideDownSum = null
  for (let i = 0; i < currRow.length; i++) {
    if (currRow[i] > currNum) {
      console.log(currRow[i], '>', currNum, '<-- Znalazlem wieksza liczbe')
      biggerNum = currRow[i]
      biggerNumIdx = i
      slideDownSum = countingSlideDownSum(pyramid, biggerNumIdx)
    }
  }
  return slideDownSum
    ? {
        sum: slideDownSum,
        idx: biggerNumIdx,
      }
    : null
}

function countingSlideDownSum(pyramid, currIdx) {
  //console.log(pyramid, currIdx, 'whats up?')
  let sum = 0
  for (let i = pyramid.length - 1; i >= 0; i--) {
    // console.log(pyramid[i], 'do gory! obecny rząd')
    sum += pyramid[i][currIdx]
    if (currIdx == 0) {
      currIdx = 0
    } else if (currIdx == pyramid[i].length - 1) {
      currIdx -= 1
    } else if (pyramid[i - 1][currIdx] < pyramid[i - 1][currIdx - 1]) {
      currIdx = currIdx - 1
    }
  }
  //console.log('alternatywna suma >>', sum, '<<')
  return sum
}
//checkingSlideDownSum([[3], [7, 4], [2, 4, 6], [8, 5, 9, 999]], 0, 3)

// longestSlideDown([
//   [75],
//   [95, 64],
//   [17, 47, 82],
//   [18, 35, 87, 10],
//   [20, 4, 82, 47, 65],
//   [19, 1, 23, 75, 3, 34],
//   [88, 2, 77, 73, 7, 63, 67],
//   [99, 65, 4, 28, 6, 16, 70, 92],
//   [41, 41, 26, 56, 83, 40, 80, 70, 33],
//   [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
// ])

//                   [75],
//                 [95, 64],
//               [17, 47, 82],
//             [18, 35, 87, 10],
//           [20,  4, 82, 47, 65],
//         [19,  1, 23, 75,  3, 34],
//       [88,  2, 77, 73,  7, 63, 67],
//     [99, 65,  4, 28,  6, 16, 70, 92]
//   [41, 41, 26, 56, 83, 40, 80, 70, 33],
// [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],

longestSlideDown([[1], [1, 1], [1, 4, 1], [1, 2, 1, 2], [1, 1, 1, 4, 1]])

//        [1],
//      [1, 1],
//     [1, 4, 1],
//   [1, 2, 1, 2],
//  [1, 1, 1, 4, 1],
