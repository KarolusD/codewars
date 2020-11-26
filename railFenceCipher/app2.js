function encodeRailFenceCipher(string, numberRails) {
  let currRail = 0
  let goDown = true
  let rails = []
  for (let i = 0; i < string.length; i++) {
    rails[currRail]
      ? (rails[currRail] += string[i])
      : (rails[currRail] = string[i])

    if (currRail == numberRails - 1) {
      goDown = false
    } else if (currRail == 0) {
      goDown = true
    }
    currRail < numberRails - 1 && goDown ? currRail++ : currRail--
  }
  return rails.join('')
}

function decodeRailFenceCipher(string, numberRails) {
  const elementsInRails = numberOfElementsInRails(string, numberRails)
  const rails = buildingRails(string, elementsInRails)
  let goDown = true
  let currRail = 0
  let currRailsLetter = []
  let decodedMsg = ''

  for (let i = 0; i < string.length; i++) {
    if (!currRailsLetter[currRail]) currRailsLetter[currRail] = 0

    let currRailLetter = currRailsLetter[currRail]

    if (rails[currRail][currRailLetter]) {
      decodedMsg += rails[currRail][currRailLetter]
    }

    if (currRail == numberRails - 1) {
      goDown = false
    } else if (i !== 0 && currRail == 0) {
      goDown = true
    }

    currRailsLetter[currRail] += 1
    goDown ? currRail++ : currRail--
  }
  return decodedMsg
}

function buildingRails(string, elementsInRails) {
  let currRailsLetter = 0
  let rails = []
  for (let i = 0; i < elementsInRails.length; i++) {
    for (
      let j = currRailsLetter;
      j < currRailsLetter + elementsInRails[i];
      j++
    ) {
      rails[i] ? (rails[i] += string[j]) : (rails[i] = string[j])
    }
    currRailsLetter += elementsInRails[i]
  }
  return rails
}

function numberOfElementsInRails(string, numberRails) {
  let currRail = 0
  let goDown = true
  let elementsInRails = []
  for (let i = 0; i < string.length; i++) {
    elementsInRails[currRail]
      ? (elementsInRails[currRail] += 1)
      : (elementsInRails[currRail] = 1)

    if (currRail == numberRails - 1) {
      goDown = false
    } else if (currRail == 0) {
      goDown = true
    }
    currRail < numberRails - 1 && goDown ? currRail++ : currRail--
  }
  return elementsInRails
}

//console.log(encodeRailFenceCipher('Hello, World!', 3))
console.log(decodeRailFenceCipher('Hoo!el,Wrdl l', 3))
