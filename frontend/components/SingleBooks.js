import React, { useEffect, useState } from 'react'
import axios from 'axios'


const SingleBook = (props) => {

  const bookId = props.match.params.bookId
  console.log(props)
  const [book, updateBook] = useState({})
  const [comments, updateComments] = useState(true)

  useEffect(()  => {
    axios.get(`/api/books/${bookId}`)
      .then((resp) => {
        updateBook(resp.data)
        console.log(resp.data)
      })
  }, [])

  function handleComment() {
    updateText('')
    axios.post(`/api/books/${id}/comments`, { text }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(resp => {
        axios.get(`/api/books/${bookid}`, {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
          // .then(resp => updateBook(resp.data))
      })
  }




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
            <div className='li' className='a' class="breadcrumb-item"><a>Genre</a></div>
            <div className='li' className='a' class="breadcrumb-item"><a>{book.age}</a></div>
          </div>
      </nav>
    </div>
    </div>
    {/* <div class="column-xs-12 column-md-5" class="grid product"> */}
    {/* <div class="column-xs-12 column-md-7"> */}
    {/* <div class="product-image"> */}
    <div className="columns is-multiline is-mobile">
    <div className="column is-one-third-desktop is-half-tablet is-half-mobile"></div>
    <img className='imagezoom' src={book.image} alt={book.title} />
    <div class="description">
        <h1 className='h2' >{book.title}</h1>
        <h2 className='h1' >{book.author}</h2>
        
          <p>{book.description}</p>
          <button class="readmore"><a href ={book.read}> Read More </a></button>
        </div>
    </div>
    
        
    {/* </div> */}
    {/* </div> */}
    {/* </div> */}
    <div className="one-event-comments">
        <div className="add-comment">
          <textarea  className="textarea" placeholder="Add a comment..."></textarea>
        </div>
      </div>
    {/* <div class="column-xs-12 column-md-5"> */}
    </div>

      {/* </div> */}
      {/* </div> */}

  
  </main>
  
 
  
}


export default SingleBook