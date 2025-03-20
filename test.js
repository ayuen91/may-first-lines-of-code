let number = parseInt(prompt('Enter a number: '));
function evenOrOdd(number) {
  if (number % 2 == 0) {
    return 'Even';
  } else {
    return 'Odd';
  }
}

console.log(evenOrOdd(number));