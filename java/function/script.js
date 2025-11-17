console.log("hello console");
function myfun(){
    console.log("i am funtion")
}
myfun();

function sum(a,b){
    let c = a+b;
    console.log(c);
}
sum(10,20);

function sub(x,y){
    // let d = x-y;
    // console.log(d)
    return x-y;

}
let subrest = sub(30,10);
console.log(subrest*3);

function greet(name){
    console.log(`Hello ${name}, welocome to wesite`)
}
greet("shipon");


//Arrow function
const multiply =(x,y) => x*y;
console.log(multiply(5,10));