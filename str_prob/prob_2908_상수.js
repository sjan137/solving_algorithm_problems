let input = require("fs").readFileSync("test.txt").toString().trim();
let newInput = "";

for (let i = input.length - 1; i >= 0; i--) {
  newInput += input[i];
}

let result = Math.max(...newInput.split(" ").map((n) => Number(n)));
console.log(result);
