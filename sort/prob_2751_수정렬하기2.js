let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((num) => Number(num));
let arr = input.slice(1);
arr.sort((a, b) => a - b);

console.log(arr.join("\n"));
