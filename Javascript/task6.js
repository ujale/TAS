//Task 6 (Revised task)
const side1 = 5
const side2 = 2
const side3 = 4

if(side1 === side2 && side2 === side3 && side1 === side3){
    console.log('Equilateral triangle')
}else if(side1 === side2 || side2 === side3 || side1 === side3){
    console.log('Isosceles triangle')
}else{
    console.log('Scalene triangle')
}