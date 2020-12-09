import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
// import { getUserId } from ''

const User = (props) => {

  console.log(props)
  const userId = props.match.params.userId
  console.log(userId)
  const [user, updateUser] = useState([])
  const [comments, updateComments] = useState([])
  const username = localStorage.getItem('username')
  // const userAvatar = localStorage.getItem('userAvatar')

  // ! Get user ID //
  useEffect(() => {
    axios.get(`/api/users/${userId}`)
      .then(resp => {
        updateUser(resp.data)
        console.log(resp.data)
      })
  }, [])

  // ! Get user's comments //
  //! This is the route to get all the comments associated with the book
  //@router.route('/books/<int:book_id>/comments/<int:comment_id>', methods=['GET'])
  //useEffect(() => {
  //  axios.get(`/api/users/${userId}/comments`)
  //    .then(resp => {
  //      updateComments(resp.data)
  //    })
  //}, [])

  // ! Loading screen //
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

  return <section className='background-img'>
    <div>
      <h2 className='userTitle'>Profile</h2>
      {/* <h2 className='userSubTitle'>{userId}</h2>
      <h2 className='userSubTitle'>{username}</h2> */}
    </div>
  </section>

  //  {/* Load the user's comments and avatar */}
  //  <div>
  //    {comments[0] && <div>
  //      <h2 className='userComments'>{user.username}'s comments:</h2>
  //      <div>
  //        {comments.map(comment => {
  //          return <div key={comment.comment._id}>
  //            <figure>
  //              <p>
  //                <img src={userAvatar} />
  //              </p>
  //            </figure>
  //            <div>
  //              <p>
  //                {comment.comment.text}
  //              </p>
  //            </div>
  //          </div>
  //        })}
  //      </div>
  //    </div>}
  //  </div>

}

export default User
