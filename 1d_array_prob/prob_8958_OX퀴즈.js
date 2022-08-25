let input = require("fs").readFileSync("input.txt").toString().split("\n");
const n = Number(input[0]);
let oxs = input.slice(1).map((ox) => ox.trim());

for (let i = 0; i < n; i++) {
  const ox = oxs[i];
  let plusScore = 1;
  let score = 0;

  for (let j = 0; j < ox.length; j++) {
    if (ox[j] === "O") {
      score += plusScore;
      plusScore += 1;
    } else {
      plusScore = 1;
    }
  }

  console.log(score);
}
