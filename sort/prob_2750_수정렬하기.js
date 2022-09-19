let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .trim()
  .split("\n")
  .map((num) => Number(num));
let arr = input.slice(1);
arr.sort((a, b) => a - b);

for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
