let input = require("fs").readFileSync("test.txt").toString().trim().split(" ");
console.log(input[0] === "" ? 0 : input.length);
