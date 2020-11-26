const removeDuplicateIds = (obj) => {
  const properties = Object.keys(obj).reverse()
  let hashArr = new Set()

  properties.forEach((prop) => {
    obj[prop] = [...new Set(obj[prop])] // get rid of duplicates in array
    let objElem = obj[prop] // current array element in obj (after removing duplicates)

    for (let j = objElem.length - 1; j >= 0; j--) {
      if (hashArr.has(objElem[j])) {
        obj[prop].splice(j, 1) // remove any other duplicates in arrays above
      }
    }
    // set hash array with all letters that were already iterated
    hashArr = new Set(objElem.concat(...hashArr))
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
