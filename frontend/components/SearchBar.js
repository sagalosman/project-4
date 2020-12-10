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
    <h2> Search Bar </h2>

    <input className="search-bar"
      placeholder="Enter the book name ..."
      onChange = {(event) => updateWords(event.target.value)}
      value = {words}
      onKeyPress = {enterKey}
    />


  </div>
}


export default SearchBar