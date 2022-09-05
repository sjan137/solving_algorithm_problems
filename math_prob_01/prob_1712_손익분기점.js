let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((item) => Number(item));
let [a, b, c] = input;
let result = -1;

if (c - b > 0) {
  a % (c - b) === 0
    ? (result = parseInt(a / (c - b) + 1))
    : (result = Math.ceil(a / (c - b)));
}

console.log(result);
