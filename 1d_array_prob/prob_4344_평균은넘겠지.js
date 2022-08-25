let input = require("fs").readFileSync("input.txt").toString().split("\n");
const n = Number(input[0]);
let classes = input
  .slice(1)
  .map((row) => row.split(" ").map((item) => Number(item)));

const getOverAvg = (arr) => {
  const n = arr[0];
  let myClass = arr.slice(1);
  let sum = myClass.reduce((sum, score) => sum + score, 0);
  let avg = sum / n;
  let overCnt = 0;

  for (let i = 0; i < n; i++) {
    if (myClass[i] > avg) overCnt += 1;
  }

  return ((100 * overCnt) / n).toFixed(3);
};

for (let i = 0; i < n; i++) {
  console.log(`${getOverAvg(classes[i])}%`);
}
