let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let arr = input[1].split(" ").map((n) => Number(n));
let cnt = 0;

for (let i = 0; i < input[0]; i++) {
  if (arr[i] === 1) continue;
  let start = 2;
  let end = Math.sqrt(arr[i]);

  while (start <= end) {
    if (arr[i] % start === 0) break;
    start++;
  }

  if (start > end) cnt++;
}

console.log(cnt);
