let input = Number(require("fs").readFileSync("test.txt").toString());
let fiveSugar = parseInt(input / 5);
let result = -1;

while (fiveSugar >= 0) {
  let sugarRemained = input - fiveSugar * 5;

  if (sugarRemained % 3 === 0) {
    result = fiveSugar + parseInt(sugarRemained / 3);
    break;
  } else {
    fiveSugar--;
  }
}

console.log(result);
