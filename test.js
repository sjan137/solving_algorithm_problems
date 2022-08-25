let input = require("fs").readFileSync("test.txt").toString().split("\n");
let totalPrice = Number(input[0]);
let totalCnt = Number(input[1]);
let checkPrice = 0;

for (i = 2; i < 2 + totalCnt; i++) {
  console.log(input[i]);
  let bought = input[i].split(" ").map((item) => Number(item));
  checkPrice += bought[0] * bought[1];
}

console.log(totalPrice == checkPrice ? "Yes" : "No");
