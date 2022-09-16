let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split("\n")
  .map((num) => Number(num));
const countPrime = (n) => {
  let start = n + 1;
  let end = 2 * n;
  let cnt = 0;

  for (let i = start; i <= end; i++) {
    if (isPrime(i)) cnt++;
  }

  return cnt;
};

const isPrime = (n) => {
  if (n === 2) return true;
  else if (n < 2 || n % 2 === 0) return false;
  let start = 3;
  let end = Math.ceil(Math.sqrt(n));

  while (start <= end) {
    if (n % start === 0) return false;
    start += 2;
  }

  return true;
};

for (let i = 0; i < input.length; i++) {
  if (input[i] === 0) break;
  console.log(countPrime(input[i]));
}
