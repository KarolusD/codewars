function sumIntervals(intervals) {
  let sum = 0
  const sIntervals = intervals.sort((a, b) => b[0] - a[0])
  for (let i = sIntervals.length - 1; i >= 0; i--) {
    if (i == 0 || sIntervals[i][1] <= sIntervals[i - 1][0]) {
      sum += sIntervals[i][1] - sIntervals[i][0]
    } else {
      sIntervals[i - 1] =
        sIntervals[i - 1][1] > sIntervals[i][1]
          ? [sIntervals[i][0], sIntervals[i - 1][1]]
          : sIntervals[i]
    }
  }
  return sum
}

var test2 = [
  [1, 4],
  [7, 10],
  [3, 5],
]

//sumIntervals(test1) //4
sumIntervals(test2) //7
