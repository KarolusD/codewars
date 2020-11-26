function solve(arr) {
  let sArr = arr.sort((a, b) => a - b)
  let days = 0

  while (sArr[2] > 0) {
    sArr[1] -= 1
    sArr[2] -= 1
    days++
    sArr = sArr[1] < sArr[0] ? sArr.sort((a, b) => a - b) : sArr
  }
  return days
}

console.log(solve([1, 1, 1]), 1)
console.log(solve([1, 2, 1]), 2)
console.log(solve([4, 1, 1]), 2)
console.log(solve([8, 2, 8]), 9)
console.log(solve([8, 1, 4]), 5)
console.log(solve([7, 4, 10]), 10)
console.log(solve([12, 12, 12]), 18)
console.log(solve([1, 23, 2]), 3)
