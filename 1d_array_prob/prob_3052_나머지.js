let input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((item) => Number(item) % 42);
let set = new Set(input);

console.log(set.size);
