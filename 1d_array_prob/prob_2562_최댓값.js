let input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .split("\n")
  .map((item, idx) => [Number(item), idx + 1]);
// let maxNum = 0;
// let maxIdx = -1;

// for (let i = 0; i < 9; i++) {
//   if (maxNum < input[i][0]) {
//     maxNum = input[i][0];
//     maxIdx = i + 1;
//   }
// }

// console.log(`${maxNum}\n${maxIdx}`);

let n = input.length;
console.log(n);
input.sort((a, b) => a[0] - b[0]);
console.log(`${input[9][0]}\n${input[9][1]}`);
