// 9. Return the number of vowels in a string
function countVowels(string) {
    const vowels = ["a", "e", "u", "i", "o"];
    let numberOfVowels = 0;
   
    for (let i = 0; i < string.length; i++) {
     if (vowels.includes(string[i].toLowerCase())) {
      numberOfVowels++;
     }
    }
    return numberOfVowels;
   }
   
   console.log(countVowels("Famous Amos Biscuit"));
   