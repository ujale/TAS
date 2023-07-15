//Task 14
const books = [
        {
            title: 'Peter Pan',
            description: 'Storybook',
            numberOfPages: 12,
            author: "William murphy",
            reading: false
        },
        {
            title: 'Famous 5',
            description: 'Adventure',
            numberOfPages: 15,
            author: "Benjamin Thomas",
            reading: true
        },
        {
            title: 'Gulliver travel',
            description: 'Mystery',
            numberOfPages: 32,
            author: 'Gordon Brown',
            reading: true
        },
        {
            title: 'Book of Moses',
            description: 'Religious',
            numberOfPages: 19,
            author: 'Moses Peter',
            reading: false
        }
    ]
    for(let i = 0; i<= books.length; i++){
        if(books[i].reading === true){
            console.log(books[i])
        }
    }