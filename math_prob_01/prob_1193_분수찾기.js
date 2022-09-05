let input = Number(require("fs").readFileSync("test.txt").toString());
// 1 - 2 - 3 - 4 - 5 - ... (짝수는 왼쪽부터, 홀수는 오른쪽부터)
let row = 1;
let rowMaxNum = 1;
let leftStart = true;

while (input > rowMaxNum) {
  row++;
  rowMaxNum += row;
  leftStart = !leftStart;
}

let result = "";
let diff = rowMaxNum - input;

leftStart
  ? (result = `${1 + diff}/${row - diff}`)
  : (result = `${row - diff}/${1 + diff}`);
console.log(result);
