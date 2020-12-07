import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

const User = (props) => {

  console.log(props)
  const userId = props.match.params.userId
  const [user, updateUser] = useState([])
  const [comments, updateComments] = useState([])
  const username = localStorage.getItem('username')
  //  const userAvatar = localStorage.getItem('userAvatar')

  // Get user ID //
  useEffect(() => {
    axios.get(`/api/users/${userId}`)
      .then(resp => {
        updateUser(resp.data)
        console.log(resp.data)
      })
  }, [])

  // Get user's comments //
  useEffect(() => {
    axios.get(`/api/users/${userId}/comments`)
      .then(resp => {
        updateComments(resp.data)
      })
  }, [])

  // Loading screen //
  //  if (!user.username) {
  //    return <div className="section">
  //      <div className="container">
  //        <div className="title">
  //          Loading ...
  //        </div>
  //        <progress className="progress is-small is-link" max="100">80%</progress>
  //      </div>
  //    </div>
  //  }

  return <div><h2></h2>
    <div>
      <h5>{userId} Test 1</h5>
      <h5>{username} Test 2</h5>
    </div>
    {/* Load the user's comments */}
    <div>
      {comments[0] && <div>
        <h6>{user.username}'s comments:</h6>
        <div>
          {comments.map(comment => {
            return <div key={comment.comment._id}>
              <figure>
                <p>
                  <img src={userAvatar} />
                </p>
              </figure>
              <div>
                <p>
                  {comment.comment.text}
                </p>
              </div>
            </div>
          })}
        </div>
      </div>}
    </div>

  </div>

}

export default User

