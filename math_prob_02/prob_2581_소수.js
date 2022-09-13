let [M, N] = require("fs")
  .readFileSync("test.txt")
  .toString()
  .split("\n")
  .map((num) => Number(num));
let primeSum = 0;
let minPrime = -1;
let isMin = true;
const isPrime = (num) => {
  if (num === 2) return true;
  if (num === 1 || num % 2 === 0) return false;
  let start = 3;
  let end = Math.ceil(Math.sqrt(num));

  while (start <= end) {
    if (num % start === 0) return false;
    start += 2;
  }

  return true;
};

for (let i = M; i <= N; i++) {
  if (isPrime(i)) {
    if (isMin) {
      minPrime = i;
      isMin = false;
    }
    primeSum += i;
  }
}

minPrime < 0 ? console.log(-1) : console.log(`${primeSum}\n${minPrime}`);
