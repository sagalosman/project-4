import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import { getUserId } from '../lib/auth'

const UserProfile = (props) => {
  // console.log(props)
  const token = localStorage.getItem('token')


  const [user, updateUser] = useState({})
  const [userBooks, updateUserBooks] = useState([])


  useEffect(() => {
    axios.get(`/api/users/${getUserId()}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(resp => {
        updateUser(resp.data)

      })
  }, [])
  console.log(user)

  useEffect(() => {
    axios.get(`/api/user-books/${getUserId()}`)
      .then(resp => {
        updateUserBooks(resp.data)
      })
  }, [])

  console.log(userBooks)

  // ! Loading screen //
  if (!user.username) {
    return <div className="section">
      <div className="container">
        <div className="title">
          Loading ...
        </div>
        <progress className="progress is-small is-link" max="100">80%</progress>
      </div>
    </div>
  }

  return <section style={{ marginLeft: '40px'}}>
    <div>
      <h2>Welcome {user.name} !</h2>
      <h2 >{user.username}</h2> 
    </div>

    <div>
      {userBooks.books && userBooks.books.map((book,index) => {
        return <div key={index}  >
          <div style={{ marginTop: '100px'}} className= "card" >
            <img src={book.image}  alt={book.title} style={{ height: '40%', width: '40%' }} />
            <h2 style={{ fontSize: '24px' }}>{book.title} </h2>
            <p style={{ fontSize: '14px' }} >{book.author} </p>

          </div>

        </div>
      })}

    </div>
  </section>

}

export default UserProfile
