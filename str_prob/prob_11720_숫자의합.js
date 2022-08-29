let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let nums = input[1].split("").map((i) => Number(i));
let result = nums.reduce((sum, num) => sum + num, 0);
console.log(result);
