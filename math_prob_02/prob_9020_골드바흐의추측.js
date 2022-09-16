let input = require("fs")
  .readFileSync("test.txt")
  .toString()
  .trim()
  .split("\n")
  .map((num) => Number(num));
let T = input[0];
let cases = input.slice(1);
let isPrimeArr = Array(10000).fill(false);

// 소수인지 판별하는 함수
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

// 가장 차이가 적은 골드바흐 파티션을 배열로 리턴하는 함수
const getGBP = (n, arr) => {
  let leftIdx = n / 2;
  let rightIdx = n / 2;

  while (!(arr[leftIdx - 1] && arr[rightIdx - 1])) {
    leftIdx--;
    rightIdx++;
  }

  return `${leftIdx} ${rightIdx}`;
};

isPrimeArr[1] = true; // 소수 여부 배열 중 2는 true로 변경
// 소수 여부 배열 중 3 이상의 모든 홀수에 대해 소수 여부 반영
for (let i = 2; i < isPrimeArr.length; i += 2) {
  isPrimeArr[i] = isPrime(i + 1);
}

for (let i = 0; i < T; i++) {
  console.log(getGBP(cases[i], isPrimeArr));
}
