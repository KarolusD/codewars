// sort your hand 2 -> A i.e [ 'TC', 'JS', 'QS', 'KH', 'AH' ]
// sort opponent hand 2 -> A
// determine your hand somehow i.e you have 'Full House'
// determine opponent's hand i.e he has 'Two Pairs'
// compare your hand with opponent's hand

// array for holding suits to determine i.e flush or straight
// array for holding values to determine i.e four of kind, full house,
// three of kind, two pairs, pairs

const Result = { win: 1, loss: 2, tie: 3 }
const cardRank = [
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  'T',
  'J',
  'Q',
  'K',
  'A',
]
const handValues = [
  'High card',
  'Pair',
  'Two pairs',
  'Three of a kind',
  'Straight',
  'Flush',
  'Full house',
  'Four of a kind',
  'Straight flush',
  'Royal flush',
]

function PokerHand(hand) {
  this.hand = this.sortHand(hand)
}

PokerHand.prototype.compareWith = function (hand) {
  const myHandValue = this.determineHandValue(this.hand)
  const opponentHandValue = this.determineHandValue(hand)
  console.log(myHandValue, opponentHandValue)

  if (handValues.indexOf(myHandValue) > handValues.indexOf(opponentHandValue)) {
    return Result.win
  } else if (
    handValues.indexOf(myHandValue) < handValues.indexOf(opponentHandValue)
  ) {
    return Result.loss
  } else {
    if (myHandValue === 'Straight' || myHandValue === 'High card') {
      const myHighestCard = this.hand[0]
      const opponentHighestCard = hand[0]
      if (
        cardRank.indexOf(myHighestCard[0]) >
        cardRank.indexOf(opponentHighestCard[0])
      ) {
        return Result.win
      } else if (
        cardRank.indexOf(myHighestCard[0]) <
        cardRank.indexOf(opponentHighestCard[0])
      ) {
        return Result.loss
      } else {
        return Result.tie
      }
    } else if (myHandValue == 'Pair' || myHandValue == 'Two Pairs') {
      return Result.tie
    }
  }
}

PokerHand.prototype.sortHand = function (hand) {
  return hand
    .split(' ')
    .sort((a, b) => cardRank.indexOf(a[0]) - cardRank.indexOf(b[0]))
}

PokerHand.prototype.determineHandValue = function (hand) {
  const highestCard = hand[4]
  let straight = null
  let flush = null
  let pairs = []

  const handValues = new Set()
  const handSuits = new Set()

  for (let i = 0; i < hand.length; i++) {
    let cardValue = hand[i][0]
    let cardSuit = hand[i][1]

    handValues.add(cardValue)
    handSuits.add(cardSuit)

    if (!pairs[0]) {
      pairs[0] = [cardValue]
    } else if (pairs[0].indexOf(cardValue) !== -1) {
      pairs[0].push(cardValue)
    } else if (!pairs[1]) {
      pairs[1] = [cardValue]
    } else if (pairs[1].indexOf(cardValue) !== -1) {
      pairs[1].push(cardValue)
    }

    if (i == 4) {
      if (pairs[1] && pairs[1].length < 2) pairs.splice(1, 1)
      if (pairs[0] && pairs[0].length < 2) pairs.splice(0, 1)
      if (pairs.length !== 0) {
        pairs.sort((a, b) => cardRank.indexOf(a[0]) - cardRank.indexOf(b[0]))
      }
      console.log(pairs, 'parki')
    }
  }

  straight =
    cardRank.indexOf(hand[4][0]) - cardRank.indexOf(hand[0][0]) === 4
      ? true
      : false

  flush = handSuits.size === 1 ? true : false

  if (straight && flush && highestCard[0] === 'A') {
    return ['Royal flush']
  } else if (straight && flush) {
    return ['Straight']
  } else if (handValues.size === 2 && hand[1][0] == hand[3][0]) {
    return ['Four of kind', pairs]
  } else if (handValues.size === 2) {
    return ['Full house', pairs]
  } else if (flush) {
    return ['Flush']
  } else if (straight) {
    return ['Straight']
  } else if (
    handValues.size === 3 &&
    ((pairs[0] && pairs[0].length == 3) || (pairs[1] && pairs[1].length == 3))
  ) {
    return ['Three of kind', pairs]
  } else if (handValues.size === 3) {
    return ['Two pairs', pairs]
  } else if (handValues.size === 4) {
    return ['Pair', pairs]
  } else {
    return ['High card']
  }
}

function assert(expected, player, opponent) {
  var p = new PokerHand(player)
  var o = new PokerHand(opponent)
  console.log(p.compareWith(o.hand), expected)
}

assert(Result.loss, '2H 3H 4H 5H 6H', 'KS AS TS QS JS')

assert(Result.win, '2H 3H 4H 5H 6H', 'AS AD AC AH JD')
assert(Result.win, 'AS AH 2H AD AC', 'JS JD JC JH 3D')
assert(Result.loss, '2S AH 2H AS AC', 'JS JD JC JH AD')

assert(Result.win, '2S AH 2H AS AC', '2H 3H 5H 6H 7H')

assert(Result.win, 'AS 3S 4S 8S 2S', '2H 3H 5H 6H 7H')
assert(Result.win, '2H 3H 5H 6H 7H', '2S 3H 4H 5S 6C')
assert(Result.tie, '2S 3H 4H 5S 6C', '3D 4C 5H 6H 2S')
assert(Result.win, '2S 3H 4H 5S 6C', 'AH AC 5H 6H AS')
assert(Result.loss, '2S 2H 4H 5S 4C', 'AH AC 5H 6H AS')

assert(Result.win, '2S 2H 4H 5S 4C', 'AH AC 5H 6H 7S')
assert(Result.loss, '6S AD 7H 4S AS', 'AH AC 5H 6H 7S')

assert(Result.loss, '2S AH 4H 5S KC', 'AH AC 5H 6H 7S')

assert(Result.loss, '2S 3H 6H 7S 9C', '7H 3C TH 6H 9S')

assert(Result.win, '4S 5H 6H TS AC', '3S 5H 6H TS AC')
assert(Result.tie, '2S AH 4H 5S 6C', 'AD 4C 5H 6H 2C')
