let input = Number(require("fs").readFileSync("/dev/stdin").toString());
// 1 - 6 - 12 - 18 - 24 - ...
let line = 0;
let lineMaxNum = 1;

while (input > lineMaxNum) {
  line += 1;
  lineMaxNum += 6 * line;
}

console.log(line + 1);
