const removeDuplicateIds = (obj) => {
  console.log(Object.keys(obj).reverse(), 'keys')
  const properties = Object.keys(obj).reverse()
  let hashArr = new Set([...obj[properties[0]]])
  console.log(hashArr.has('A'), 'teeest')
  console.log(hashArr, 'hashArr initial')
  properties.forEach((prop) => {
    for (let i = obj[prop].length - 1; i >= 0; i--) {
      obj[prop] = [...new Set(obj[prop])]
      if (hashArr.has(obj[prop][i])) {
        console.log(obj[prop], obj[prop][i], '<-- delete elem from array')
        obj[prop].splice(i, 1)
      }
      console.log(obj[prop], 'after delete')
    }
    hashArr.add(...obj[prop])
  })
  return obj
}

// const obj = {
//   '1': ['A', 'B', 'C'],
//   '2': ['A', 'B', 'D', 'A'],
// }
// const result = removeDuplicateIds(obj)

// const obj1 = {
//   '1': ['C', 'F', 'G'],
//   '2': ['A', 'B', 'C'],
//   '3': ['A', 'B', 'D'],
// }
// const result1 = removeDuplicateIds(obj1)

// const obj2 = {
//   '1': ['A'],
//   '2': ['A'],
//   '3': ['A'],
// }
// const result2 = removeDuplicateIds(obj2)

const obj3 = {
  '11': ['P', 'R', 'S', 'D'],
  '53': ['L', 'G', 'B', 'C'],
  '236': ['L', 'A', 'X', 'G', 'H', 'X'],
  '432': ['A', 'A', 'B', 'D'],
}
const result3 = removeDuplicateIds(obj3)

// console.log(result1)
// console.log(result2)
console.log(result3)
