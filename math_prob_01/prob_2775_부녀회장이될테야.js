let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split("\n")
  .map((num) => Number(num));
let T = input.shift();

for (let i = 0; i < T; i++) {
  let k = input.shift();
  let n = input.shift();
  let arr = Array.from(Array(k + 1), () => Array(n).fill(0));

  for (let j = 0; j < k + 1; j++) {
    for (let m = 0; m < n; m++) {
      if (j === 0) {
        arr[j][m] += m + 1;
      } else {
        arr[j][m] += m === 0 ? arr[j - 1][m] : arr[j - 1][m] + arr[j][m - 1];
      }
    }
  }

  console.log(arr[k][n - 1]);
}
