// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper(collection, itemsPerPage) {
  this.collection = collection
  this.itemsPerPage = itemsPerPage
}

// returns the number of items within the entire collection
PaginationHelper.prototype.itemCount = function () {
  return this.collection.length
}

// returns the number of pages
PaginationHelper.prototype.pageCount = function () {
  return Math.ceil(this.collection.length / this.itemsPerPage)
}

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper.prototype.pageItemCount = function (pageIndex) {
  if (pageIndex + 1 > this.pageCount()) {
    return -1
  } else if (pageIndex + 1 == this.pageCount()) {
    return this.collection.length % this.itemsPerPage
  } else {
    return this.itemsPerPage
  }
}

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper.prototype.pageIndex = function (itemIndex) {
  if (itemIndex >= 0 && itemIndex < this.collection.length) {
    return itemIndex == 0 ? 0 : Math.ceil(itemIndex / this.itemsPerPage) - 1
  } else {
    return -1
  }
}

ph = new PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
console.log(ph.itemCount())
console.log(ph.pageCount())
console.log(ph.pageItemCount(2))
console.log(ph.pageIndex(5))
