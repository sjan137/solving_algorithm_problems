// const getSelfNums = (maxNum) => {
//   let notSelfNums = new Set();

//   for (let i_4 = 0; i_4 < 10; i_4++) {
//     for (let i_3 = 0; i_3 < 10; i_3++) {
//       for (let i_2 = 0; i_2 < 10; i_2++) {
//         for (let i_1 = 0; i_1 < 10; i_1++) {
//           notSelfNums.add(1000 * i_4 + 100 * i_3 + 10 * i_2 + 2 * i_1);
//         }
//       }
//     }
//   }

//   for (let i = 1; i < maxNum + 1; i++) {
//     if (notSelfNums.has(i)) {
//       continue;
//     }
//     console.log(i);
//   }
// };

// getSelfNums(10000);

function d(n) {
  let number = n;
  let result = 0;

  for (let i = 0; i < String(n).length; i++) {
    // number를 10으로 나눠가면서 각 자리수를 result에 합한다.
    result += number % 10;
    number = Math.floor(number / 10);
  }
  // 입력받은 수 와 result를 더하여 return
  return n + result;
}

const range = 10000;
// 0~10000 범위까지 셀프넘버 배열을 생성하고 true로 초기화.
let selfNumbers = Array(range + 1).fill(true);

for (let i = 0; i <= range; i++) {
  // 셀프넘버가 아니면 false로 변환.
  selfNumbers[d(i)] = false;
}

// true index만 출력
for (let i = 0; i < range; i++) {
  if (selfNumbers[i]) {
    console.log(i);
  }
}
