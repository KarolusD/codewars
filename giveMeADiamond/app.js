function diamond(n) {
  if (n % 2 === 0 || n <= 0) return null
  let spaces = ''
  let count = n
  let diamMid = Math.floor(n / 2)
  let diam = asterisk(count) // start from middle
  for (let i = 0; i < diamMid; i++) {
    spaces += ' '
    count -= 2
    let row = spaces + asterisk(count)
    diam += row // adding down row
    diam = row + diam // adding up row
  }
  return diam
}

function asterisk(count) {
  let asterisks = ''
  for (let i = 0; i < count; i++) {
    asterisks += '*'
  }
  return asterisks + '\n'
}

console.log(diamond(3))
