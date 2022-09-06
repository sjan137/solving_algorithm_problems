let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split(" ")
  .map((num) => Number(num));
let [a, b, c] = input;
let result = Math.ceil((c - b) / (a - b));

console.log(result);
