let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .trim()
  .toUpperCase();
let arr = Array(26).fill(0);
let maxCnt = 0;
let result = "";
const start = "A".charCodeAt();

for (let i = 0; i < input.length; i++) {
  let idx = input[i].charCodeAt() - start;
  arr[idx]++;
  if (arr[idx] > maxCnt) {
    maxCnt = arr[idx];
    result = String.fromCharCode(idx + start);
  }
}

arr.sort((a, b) => b - a);

if (arr[0] === arr[1]) result = "?";

console.log(result);
