const hanCheck = (num) => {
  let a_1 = num % 10;
  num = parseInt(num / 10);
  let a_2 = num % 10;
  const d = a_1 - a_2;
  let new_d = 0;

  while (num >= 10) {
    a_1 = num % 10;
    num = parseInt(num / 10);
    a_2 = num % 10;
    new_d = a_1 - a_2;

    if (new_d != d) return false;
  }

  return true;
};

let input = parseInt(require("fs").readFileSync("input.txt").toString());
let cnt = 0;

if (input < 100) {
  cnt = input;
} else {
  cnt = 99;

  for (let i = 100; i <= input; i++) {
    if (hanCheck(i)) {
      cnt++;
    }
  }
}

console.log(cnt);
