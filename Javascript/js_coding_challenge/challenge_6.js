// 6. Sort an array of strings in alph. order
function sortStringArray(stringArray) {
    let newArr = [];
    const sorted = stringArray.sort();
    for (let i = 0; i < stringArray.length; i++) {
     newArr.push(stringArray[i].toLowerCase());
    }
    return newArr.sort();
   
    // NB: You can combine sort and reverse to changer the order of sorting
    //return newArr.sort().reverse()
   }
   
   console.log(sortStringArray(["jan", "Feb", "march", "April", "May","June", "July", "August", "September", "October", "November", "December" ]));