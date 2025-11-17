/* document.write("This is external link <br>");


console.log("Hello Console");

var name = "Sobuj";

let age = 30;

const PI = 3.14;

document.write(age);

function testFun(){
    var firstName = "Sobuj";
    if(true){
        var firstName = "Ahmed";
        console.log(firstName);
    }
    console.log(firstName);
}
testFun();

function testFunLet(){
    let address = "Dhaka";
    if(true){
        let address = "Rajshahi";
        console.log(address);
    }
    console.log(address);
}

testFunLet();



//Primitive Types
let age = 25;
let name = "Sobuj";
let isAdult = true;
let empty=null;
let notAssigned;

//Refference Types

let object = {name:"Sobuj",age:30,address:"Dhaka, Bangladesh"};

let array = ["red","green","blue"];

document.write(typeof array);

*/

let age = 15;
if (age >= 18) {
    document.write("Adult <br>");
}else{
    document.write("Minor <br>");
}

let marks = 115;

if (marks>=80 && marks<=100) {
    document.write("Grade A+");
}else if(marks>=70 && marks<=79){
    document.write("Grade A");
}else if(marks>=60 && marks<=69){
    document.write("Grade A-");
}else if(marks>=50 && marks<=59){
    document.write("Grade B");
}else if(marks>=40 && marks<=49){
    document.write("Grade C");
}else if(marks>=33 && marks<=39){
    document.write("Grade D");
}else{
    document.write("Grade F <br>");
}

let weather = "Foggy";
switch (weather) {
    case "Sunny":
        document.write("Its a Sunny Day.");
        break;
    case "Cloudy":
        document.write("Its cloudy today");
        break;
    case "Foggy":
        document.write("Its Foggy today");
        break;
    case "Rainy":
        document.write("Its Raining today. Take umb");
        break;
    default:
        document.write("Unknown weather, All the best");
}


//for Loop


for(let count=4;count < 10; count++){
    document.write("<br> For Loop "+count);
}

//While Loop

let count = 2;

while(count<=10){
    document.write("<br> While Loop "+count);
    count++
}

//Do .. While loop

let countDW = 3;
do{
    document.write("<br> Do While Loop "+countDW+"<br>");
    countDW= countDW+2;
}while(countDW <= 20);

// For... In.. Loop

let students= {name:"Rahim",age:25,address:"Dhaka, Bangladesh"};

for(let key in students){
    document.write(key+":"+students[key]+"<br>");
}

