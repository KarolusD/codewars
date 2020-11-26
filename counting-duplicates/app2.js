function duplicateCount(text) {
  text = text.toLowerCase()
  return text.split('').filter(function (c, i) {
    console.log(text.indexOf(c), i, text.lastIndexOf(c))
    return text.indexOf(c) == i && text.indexOf(c) != text.lastIndexOf(c)
  }).length
}

console.log(duplicateCount('aabBbbcde'))
