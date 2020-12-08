import React, { useEffect, useState } from 'react'
import axios from 'axios'


const SingleBook = (props) => {

  const bookId = props.match.params.bookId
  console.log(props)
  const [book, updateBook] = useState({})

  useEffect(()  => {
    axios.get(`/api/books/${bookId}`)
      .then((resp) => {
        updateBook(resp.data)
        console.log(resp.data)
      })
  }, [])

  console.log(book)
  if (!book.title) {
    return <div className="section">
      <div className="container">
        <div className="title">
          Loading ...
        </div>
      </div>
    </div>
  }


  return <div className="section">
    <h2></h2>

    <div className="container">
      <h2 className="title is-4">
        {book.title}
      </h2>
      <p className="subtitle is-4">
        By {book.author}
      </p>
      <img src={book.image} alt={book.title} />
      {book.title && book.genres.map((genre, genreId) => {
        return <div key={genreId}>
          <h5>{genre.genre } </h5>
        </div>
      }) }  
      <p>Recommended age: <small> {book.age} </small></p> 
      <p> {book.description} </p>
      <p></p>
    </div>
  


  </div>
}


export default SingleBook