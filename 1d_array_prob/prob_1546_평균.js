let input = require("fs").readFileSync("input.txt").toString().split("\n");
let n = Number(input[0]);
let scores = input[1].split(" ").map((score) => Number(score));
const maxScore = Math.max(...scores);
let sum = 0;

for (let i = 0; i < n; i++) {
  sum += (100 * scores[i]) / maxScore;
}

console.log(sum / n);
