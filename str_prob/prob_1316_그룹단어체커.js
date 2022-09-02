let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split("\n")
  .trim()
  .slice(1);

const groupWordCheck = (word) => {
  let wordHash = {};

  for (let i = 0; i < word.length; i++) {
    let w = word[i];
    if (!(w in wordHash)) {
      wordHash[w] = i;
    } else {
      if (i - wordHash[w] === 1) {
        wordHash[w] = i;
      } else {
        return false;
      }
    }
  }

  return true;
};

let result = 0;

for (let word of input) {
  if (groupWordCheck(word)) {
    result += 1;
  }
}

console.log(result);
