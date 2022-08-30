let input = require("fs").readFileSync("/dev/stdin").toString().trim();
let result = Array(26).fill(-1);
const start = "a".charCodeAt();

for (let i = 0; i < input.length; i++) {
  let idx = input[i].charCodeAt() - start;
  if (result[idx] == -1) result[idx] = i;
}

console.log(result.join(" "));
