let n = Number(require("fs").readFileSync("test.txt").toString().trim());
let divNum = 2;

while (n !== 1) {
  if (n % divNum === 0) {
    console.log(divNum);
    n /= divNum;
  } else {
    divNum++;
  }
}
