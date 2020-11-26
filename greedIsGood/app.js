const score = (dice) => {
  const roll = new Map()
  let points = 0
  dice.forEach((d) => {
    roll.has(d) ? roll.set(d, roll.get(d) + 1) : roll.set(d, 1)
    if (d === 1) points += 100
    if (d === 5) points += 50
  })
  if (roll.get(1) >= 3) {
    getThree = true
    points += 1000 - 300
  } else if (roll.get(6) >= 3) {
    getThree = true
    points += 600
  } else if (roll.get(5) >= 3) {
    getThree = true
    points += 500 - 150
  } else if (roll.get(4) >= 3) {
    getThree = true
    points += 400
  } else if (roll.get(3) >= 3) {
    getThree = true
    points += 300
  } else if (roll.get(2) >= 3) {
    getThree = true
    points += 200
  }
  return points
}

console.log(score([5, 5, 5, 3, 3]), '500')

//console.log(score([4, 4, 4, 3, 3]) == 400, 'Should be 400')

//console.log(score([2, 4, 4, 5, 4]) == 450, 'Should be 450')
