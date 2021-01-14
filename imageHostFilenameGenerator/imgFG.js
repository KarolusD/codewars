function generateName() {
  name = null

  const radix = 16
  const randomFilename = Math.random().toString(radix).substr(2, 6)

  if (!photoManager.nameExists(randomFilename)) {
    name = randomFilename
  }
}

class PhotoManager {
  constructor() {
    this.imageNames = new Set(['123456'])
  }

  nameExists(name) {
    return this.imageNames.has(name)
  }

  addName(name) {
    return this.imageNames.add(name)
  }
}

photoManager = new PhotoManager()
console.log(photoManager.imageNames)

generateName()
