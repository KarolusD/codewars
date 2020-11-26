const deNico = (key, m) => {
  let encodedArr = []
  let counter = 0

  for (let i = 0; i < key.length; i++) {
    let tempArr = []
    for (let j = counter; j < m.length; j += key.length) {
      tempArr.push(m[j])
    }
    counter++
    encodedArr.push(tempArr)
  }
  indexArr = sortIdx(key)
  m = decodeArr(encodedArr, indexArr)
  console.log('encodedArr', encodedArr)
  console.log('deNico', m, encodedArr, indexArr)
  return m
}

const decodeArr = (encodedArr, indexArr) => {
  //console.log('decodeArray')
  let decodedArr = []
  for (let i = 0; i < encodedArr.length; i++) {
    decodedArr[indexArr[i]] = encodedArr[i]
  }
  console.log('decodeArr', decodedArr)
  return decodeMessage(decodedArr)
}

const decodeMessage = (decodedArr) => {
  dmessage = ''
  for (let i = 0; i < decodedArr[0].length; i++) {
    for (let j = 0; j < decodedArr.length; j++) {
      //console.log('elo', j, i, decodedArr[j].length)
      if (!decodedArr[j][i]) {
        j++
      }
      if (i < decodedArr[j].length) {
        dmessage += decodedArr[j][i]
      } else {
        break
      }
    }
  }
  console.log('decodeMessage', dmessage)
  return dmessage.trimRight()
}

const sortIdx = (key) => {
  console.log('sort')
  let arrIdx = key
    .split('')
    .map((elem, idx) => {
      return [elem, idx]
    })
    .sort((a, b) => {
      if (a[0] < b[0]) {
        return -1
      }
      if (a[0] > b[0]) {
        return 1
      }
      return 0
    })
  console.log(
    'sortIdx',
    arrIdx.map((elem) => elem[1])
  )
  return arrIdx.map((elem) => elem[1])
}

deNico('z', 'jotgr q')
// key:  nhv msg:  j lejprrqjimvennggxkabpompvguptwzlyyfi
