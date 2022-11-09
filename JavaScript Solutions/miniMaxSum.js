'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function miniMaxSum(arr) {
    let totalSum = arr.reduce((total, num) => total + num, 0)
    let resultOfSums = []
    
    arr.forEach( val => resultOfSums.push(totalSum - val) )
    resultOfSums.sort((a, b) => a - b )
    
    console.log(`${resultOfSums[0]} ${resultOfSums[4]}`)
}