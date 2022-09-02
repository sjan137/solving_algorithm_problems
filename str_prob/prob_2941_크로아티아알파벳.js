let input = require("fs").readFileSync("test.txt").toString().trim();
const croaAlphas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];

for (let croaAlpha of croaAlphas) {
  if (input.includes(croaAlpha)) {
    input = input.split(croaAlpha).join("a");
  }
}

console.log(input.length);
