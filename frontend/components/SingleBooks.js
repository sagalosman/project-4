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


  return <main>
    <div class="container">
    <div class="grid second-nav">
    <div class="column-xs-12">
      <nav className='nav'>
      <div className='ol' class="breadcrumb-list">
            <div className='li' className='a' class="breadcrumb-item">
              {book.genres.map((genre, index) => {
                  return <a key={index} >Genre:  {genre.genre} </a>
              })}
              </div>
            <div className='li' className='a' class="breadcrumb-item"><a>Recommended Age:  {book.age}</a></div>
          </div>
      </nav>
    </div>
    </div>
    <div class="column-xs-12 column-md-5" class="grid product">
    <div class="column-xs-12 column-md-7">
    <div class="product-image">
    <img className='imagezoom' src={book.image} alt={book.title} />
    </div>
    </div>
    </div>
    <div class="column-xs-12 column-md-5">
        <h1 className='h1' >{book.title}</h1>
        <h2 className='h1' >{book.author}</h2>
        <div class="description">
          <p>{book.description}</p>
          
        </div>
        <button class="readmore">Read More</button>
      </div>

    </div>
  </main>
  
 
  
}


export default SingleBook