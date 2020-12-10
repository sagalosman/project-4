import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { isCreator } from '../lib/auth'
import Bulma from 'bulma'


const SingleBook = (props) => {
  const token = localStorage.getItem('token')

  const bookId = props.match.params.bookId
  console.log(bookId)
  const [book, updateBook] = useState({})
  const [text, setText] = useState('')
  const [messages, updateMessages] = useState([])

  // ! A function to reload the page

  const refreshPage = () => {
    window.location.reload()
  }

  useEffect(() => {
    axios.get(`/api/books/${bookId}`)
      .then((resp) => {
        updateBook(resp.data)
        console.log(resp.data)
      })
  }, [])

  function handleComment(bookId) {
    axios.post(`/api/books/${bookId}/comments`, { text }, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(resp => {
        setText('')

        // updateBook(resp.data)
        updateMessages(resp.data)
      })
    // refreshPage()
  }

  console.log(messages)




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
                {book.genres && book.genres.map((genre, index) => {
                  return <a key={index} >Genre:  {genre.genre} </a>
                })}
              </div>
              <div className='li' className='a' class="breadcrumb-item"><a>Recommended Age:  {book.age}</a></div>
            </div>
          </nav>
          {/* <div className="event-num big-num" onClick={() => handleLike(likes)}>
            <p className="event-like icon-bigger"></p> {likes.likes}
          </div> */}
          {/* <button className='heart'>{book.like}</button> */}
        </div>
      </div>
      {/* <div class="column-xs-12 column-md-5" class="grid product"> */}
      {/* <div class="column-xs-12 column-md-7"> */}
      {/* <div class="product-image"> */}
      <div className="columns is-multiline is-mobile">
        <div className="column is-one-third-desktop is-half-tablet is-half-mobile"></div>
        <img className='imagezoom' src={book.image} alt={book.title} />
        <div className="description">
          <h1 className='h2' >{book.title}</h1>
          <h2 className='h1' >{book.author}</h2>

          <p>{book.description}</p>
          <button className="readmore"><a href={book.read}> Read More </a></button>
          {/* COMMENTS */}
          <h2 style={{ fontSize: '24px', fontWeight: 'bolder', textDecorationLine: 'underline' }} > COMMENTS </h2>
          {book.comments && book.comments.map((comment, index) => {

            return <div key={index} style={{ marginTop: '5px', marginLeft: '20px' }} >
              <p style={{ fontSize: '15px' }} >{comment.content} </p>
            </div>
          })}
        </div>
      </div>


      {/* </div> */}
      {/* </div> */}
      {/* </div> */}
      <div className="one-event-comments">
        <div className="add-comment">
          <textarea
            className="textarea"
            placeholder="Add a comment..."
            value={text[book.id]}
            name="content"
          >
          </textarea>
        </div>
        <button
          style={{ backgroundColor: 'yellow', height: '40px', fontSize: '20px' }}
          onClick={() => handleComment(bookId)}> Submit Your Comment
        </button>
      </div>
      {/* <div class="column-xs-12 column-md-5"> */}
    </div>

    {/* </div> */}
    {/* </div> */}


  </main>



}


export default SingleBook