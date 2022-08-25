let input = require("fs").readFileSync("input.txt").toString().split("\n");
let n = Number(input[0]);
let nums = input[1].split(" ").map((item) => Number(item));

nums.sort((a, b) => a - b);
console.log(`${nums[0]} ${nums[n - 1]}`);
