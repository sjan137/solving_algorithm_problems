let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split(" ")
  .map((n) => BigInt(n));
console.log(input.reduce((cur, sum) => cur + sum, BigInt(0)).toString());
