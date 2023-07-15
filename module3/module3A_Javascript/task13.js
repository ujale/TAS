//Task 13
const books = {
    title: 'Peter Pan',
    description: 'A storybook for kids',
    numberOfPages: 35,
    author: 'William Gerround',
    reading: true,
    toggleReadingStatus: function (){
        if(books.reading === false){
            books.reading = true
        }else{
            books.reading = true
        }
    }
}
books.toggleReadingStatus()
console.log(books.reading)