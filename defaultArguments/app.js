function defaultArguments(func, params) {
  // TODO: Program me
  console.log(func, 'eloo')
  return function () {
    return func(5, 3)
  }
}

function add(a, b) {
  return a + b
}
var add_ = defaultArguments(add, { b: 9 })
console.log(add_(10), 19)
// console.log(add_(10, 5), 15)
// var add_ = defaultArguments(add_, { b: 3 })
// console.log(add_(10), 13)
