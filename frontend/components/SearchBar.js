import React, { useEffect, useState } from 'react'
import axios from 'axios'

const SearchBar = (props) => {
  console.log(props)
  const [bookData, updateBookData] = useState([])
  const [title, updateTitle] = useState('')
  const [words, updateWords] = useState('')

  const [allBooksData, updateAllBooksData] = useState([])



  
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

  // ! I will use this function to generate random books
  function getAllBooks(){
    useEffect(() => {
      axios.get('/api/books')
        .then((resp) => {
          updateAllBooksData(resp)
          console.log(resp.data)
        })
    }, []) 
  }
  getAllBooks()
  console.log(allBooksData)
  if (!allBooksData.data) {
    return <div className = "section">
      <div className="container">
        <div className="title">
          Loading
        </div>
      </div>
    </div>
  }
  

  const allBooks = allBooksData.data
  console.log(allBooks)

  const randomIndex = Math.floor(Math.random() * allBooks.length)
  console.log(randomIndex)
  const randomBook = allBooks[randomIndex]

  console.log(randomBook)




  return <div>
    <h2> Search Bar </h2>

    <input className="search-bar"
      placeholder="Enter the book name ..."
      onChange = {(event) => updateWords(event.target.value)}
      value = {words}
      onKeyPress = {enterKey}
    />

    <div>
      <p> { randomBook.author} </p>

    </div>


  </div>
}


export default SearchBar