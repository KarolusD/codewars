function kingAllPossibleMoves(startingPos, occupiedPos) {
  const columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  const rows = ['1', '2', '3', '4', '5', '6', '7', '8']

  const columnIdx = columns.indexOf(startingPos[0])
  const rowIdx = rows.indexOf(startingPos[1])

  let columnSlice = []
  let rowSlice = []
  const allMoves = []

  if (columnIdx === 0) {
    columnSlice = columns.slice(columnIdx, columnIdx + 2)
  } else if (columnIdx === 7) {
    columnSlice = columns.slice(columnIdx - 1)
  } else {
    columnSlice = columns.slice(columnIdx - 1, columnIdx + 2)
  }

  if (rowIdx === 0) {
    rowSlice = rows.slice(rowIdx, rowIdx + 2)
  } else if (rowIdx === 7) {
    rowSlice = rows.slice(rowIdx - 1)
  } else {
    rowSlice = rows.slice(rowIdx - 1, rowIdx + 2)
  }

  for (let c of columnSlice) {
    for (let r of rowSlice) {
      if (c + r !== startingPos && occupiedPos.indexOf(c + r) === -1) {
        allMoves.push(c + r)
      }
    }
  }
  return allMoves
}

kingAllPossibleMoves('H8', ['H7', 'G7', 'G8'])
