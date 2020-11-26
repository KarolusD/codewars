function encodeRailFenceCipher(string, numberRails) {
  let encodedRails = []
  let currRail = ''
  let helper = 2
  let startPoint = 0
  for (let i = 0; i < numberRails; i++) {
    for (let j = startPoint; j < string.length; j += numberRails * 2 - helper) {
      currRail += string[j]
    }

    if (i == numberRails - 2) {
      helper = 2
      startPoint = numberRails - 1
    } else {
      helper += 2
      startPoint++
    }
    encodedRails.push(currRail)
    currRail = ''
  }
  console.log(encodedRails.join(''))
  return encodedRails.join('')
}

function decodeRailFenceCipher(string, numberRails) {
  let helper = 0
  let goDown = true
  let path = []
  for (let i = 0; i < string.length; i++) {
    if (path[helper]) {
      path[helper] += string[i]
    } else {
      path[helper] = string[i]
    }

    if (i !== 0 && helper == numberRails - 1) {
      goDown = false
    } else if (helper == 0) {
      goDown = true
    }
    if (helper < numberRails - 1 && goDown) {
      helper++
    } else {
      helper--
    }
  }
  console.log(path)
}

decodeRailFenceCipher('Hello, World!', 3)
