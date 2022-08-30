const makeRepeat = (n, s) => {
  let result = "";

  for (let i = 0; i < s.length; i++) {
    result += s[i].repeat(n);
  }

  return result;
};

let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .trim()
  .split("\n");
for (let j = 1; j < input.length; j++) {
  let row = input[j].split(" ");
  console.log(makeRepeat(Number(row[0]), row[1]));
}
