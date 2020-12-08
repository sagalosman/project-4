import React, {  useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Bulma from 'bulma'


const Books = () => {

  const [books, updateBooks] = useState([])

  useEffect(() => {
    axios.get('/api/books')
      .then((resp) => {
        updateBooks(resp.data)
        console.log(resp.data)
      })
  }, [])

  console.log(books)

  return <div className = "section">
    <h2>Explore the books!</h2>
    <div className="columns is-multiline is-mobile">
      {books.map((book, index) => {
        return <div className="column is-one-third-desktop is-half-tablet is-half-mobile" 
          key={index}> 
          <Link to={`/books/${book.id}`} >
            <div className="card">
              <div className="card-content">
                <div className="media">
                  <div className="media-content">
                    <h2 className="title is-4">
                      {book.title}
                    </h2>
                    <p className="subtitle is-4">
                      {book.author}
                    </p>
                  </div>
                </div>
              </div>
              <div className="card-image">
                <figure className="image is-4by3">
                  <img src={book.image} alt={book.title} />
                </figure>
              </div>
            </div> 
          </Link>
        </div>
      })} 
    </div>
  </div>
}

export default Books
