import React, { useEffect, useState } from 'react'
import axios from 'axios'

const User = (props) => {

  console.log(props)
  const userId = props.match.params.userId
  const [user, updateUser] = useState([])
  const [comments, updateComments] = useState([])
  const userName = localStorage.getItem('userName')
  const userAvatar = localStorage.getitem('userAvatar')

  {/* Get user ID */}  
  useEffect(() => {
    axios.get(`/api/users/${userId}`)
      .then(resp => {
        updateUser(resp.data)
      })
  }, [])

  {/* Get user's comments */}
  useEffect(() => {
    axios.get(`/api/users/${userId}`)
      .then(resp => {
        updateComments(resp.data)
      })
  }, [])

  {/* Loading screen */}
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

  return <div className="container is-fluid mt-5">
    <div className="columns">
      <div className="column">
      </div>
      <div className="column">
        <figure className="image ">
          <img className=" is-rounded" src={user.avatar} />
        </figure>
      </div>
      <div className="column"></div>
    </div>
    <div className="container is-fluid has-text-centered mt-5">
      <h1 className="title is-1 is-capitalized">{user.userName}</h1>
      <h2 className="subtitle is-3">Location: {user.city}</h2>
      <h2 className="subtitle is-3">Bio:</h2>
      <p>{user.bio}</p>
    </div>
    {comments[0] && <div className="container is-fluid mt-5">
      <h2 className="subtitle is-3">{user.username}'s comments:</h2>
      <div className="content">
        {comments.map(comment => {
          return <div key={comment.comment._id} className="media">
            <figure className="media-left">
              <p className="image is-64x64">
                <img src={userAvatar} />
              </p>
            </figure>
          </div>
        })}
      </div>
    </div>}
  </div>

}
export default User

