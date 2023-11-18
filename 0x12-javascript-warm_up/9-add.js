#!/usr/bin/node
function add(a, b) {
	let c = a + b;
}
i = Number(process.argv[2]);
j = Number(process.argv[3]);
if ((process.argv[2] == undefined && process.argv[3] == undefined) || isNaN(process.argv[2])) {
	console.log("NaN");
} else {
	console.log(add(i,j));
}
