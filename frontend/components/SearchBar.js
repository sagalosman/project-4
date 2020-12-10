import React, { useEffect, useState } from 'react'
import axios from 'axios'

const SearchBar = (props) => {
  console.log(props)
  const [bookData, updateBookData] = useState([])
  const [title, updateTitle] = useState('')
  const [words, updateWords] = useState('')

  // const [allBooksData, updateAllBooksData] = useState([])



  
  const searchFunction = (title) => {
    if (title) {
      axios.get(`/api/books/${title}`)
        .then(resp => {
  
          const bookId = resp.data.id
          console.log(bookId)
          updateBookData(resp.data)

          console.log(resp.data)
          props.history.push(`/books/${bookId}`)
        })
    }
  }


  useEffect(() => {
    return searchFunction(title)
  }, [title])


  function enterKey(event) {
    if (event.key === 'Enter') {
      updateTitle(words)
    }
  }

  console.log(words)
  console.log(bookData)


  return <div>
    {/* <h2> Search Bar </h2> */}

    <input className="search-bar"
      placeholder="Enter the book name ..."
      onChange = {(event) => updateWords(event.target.value)}
      value = {words}
      onKeyPress = {enterKey}
    />
   return <div>{book.title}</div>

  </div>
}


export default SearchBar




// import React, {  useEffect, useState } from 'react'
// import { Link } from 'react-router-dom'
// import axios from 'axios'
// import Bulma from 'bulma'
// import SearchBar from './SearchBar'


// const Search = (props) => {
//   const [books, updateBooks] = useState([])
//   const [searchBooks, updateSearchBooks] = useState('')

//   useEffect(() => {
//     axios.get('/api/books')
//       .then((resp) => {
//         updateBooks(resp.data)
//         console.log(resp.data)
//       })
//   }, [])

//   function filterBooks() {
//     const filteredBooks = books.filter(book => {
//       const title = book.title.toLowerCase()
//       const author = book.author.toLowerCase()
//       const description = book.description.toLowerCase()
//       const filterText = searchBooks.toLowerCase()

//       return title.includes(filterText) || author.includes(filterText) || description.includes(filterText)
//     })
//     return filteredBooks
//   }

//   console.log(books)

//   if (!updateBooks[0]) {
//     return <>
//       <main className="homepage">
//         <div className="display-area">
//           <h1 className="loading">Loading...</h1>
//         </div>
//       </main>
//     </>
//   }

//   return   <div>
//   <input type="text" className="input" placeholder="Search for a Book"
//     onChange={(event) => updateSearchUsers(event.target.value)}
//     value={searchUsers}
//   />
// </div>
// // {filterBooks().map((book, index) => {
// //   { console.log(book) }
// //   return <div key={index} className="event">
// //     <div className="event-left">
// //       <img className="event-img" src={book.image} alt="image" />
// //     </div>
// //     <Link to={`/books/:bookId${book._id}`} className="event-content">
// //       <h4 className="event-name">{book.title} {book.author}</h4>
// //     </Link>
// //   </div>
// // })}
  
//   // <div className = "section">
//   //   {/* <h2> Books Page</h2> */}
//   //   <div className="columns is-multiline is-mobile">
  
//   //   </div>
//   //  </div>
// }

// export default Search