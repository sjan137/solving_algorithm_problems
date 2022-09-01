let input = require("fs").readFileSync("test.txt").toString().trim();
const start = "A".charCodeAt();
let result = 0;

for (let i = 0; i < input.length; i++) {
  let alpha = input[i].charCodeAt();
  let idx = parseInt((alpha - start) / 3);

  if (idx < 6) {
    result += idx + 3;
  } else {
    if (alpha - start === 18) {
      result += 8;
    } else if (19 <= alpha - start && alpha - start < 22) {
      result += 9;
    } else {
      result += 10;
    }
  }
}

console.log(result);
