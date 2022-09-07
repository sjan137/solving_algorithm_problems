let input = require("fs").readFileSync("test.txt").toString().split("\n");
let rows = input.slice(1).map((row) =>
  row
    .trim()
    .split(" ")
    .map((num) => Number(num))
);

for (let i = 0; i < input[0]; i++) {
  let row = rows[i];
  let floor = parseInt(row[2] % row[0]);
  if (floor === 0) floor += row[0];
  let room = Math.ceil(row[2] / row[0]);
  let result = "";

  room < 10 ? (result = `${floor}0${room}`) : (result = `${floor}${room}`);
  console.log(result);
}
