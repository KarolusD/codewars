const duplicateCount = (text) => {
  lowerText = text.toLowerCase()
  return new Set(
    lowerText
      .split('')
      .filter((e, i) => lowerText.slice(i + 1).indexOf(e) !== -1)
  ).size
}

console.log(duplicateCount('aabBbbcde'))
