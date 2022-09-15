let [M, N] = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split(" ")
  .map((num) => Number(num));
const isPrime = (num) => {
  if (num < 2) return false;
  if (num === 2) return true;
  let start = 2;
  let end = Math.ceil(Math.sqrt(num));

  while (start <= end) {
    if (num % start === 0) return false;
    start++;
  }

  return true;
};

for (let i = M; i <= N; i++) {
  if (isPrime(i)) console.log(i);
}
