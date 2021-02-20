const search = document.getElementById('search');
const matchList = document.getElementById('match-list');

const searchBook = async searchText => {
    const res = await fetch ('../data/book.json');
    const book= await res/json();

    console.log(states);
}

search.addEventListener('input', () => searchBook
(search,value));

