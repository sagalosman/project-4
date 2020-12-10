import React, { useEffect, useState } from 'react'
import { getUserId } from '../lib/auth'
import axios from 'axios'




const Home = () => {
  // const [user, updateUser] = useState([])
  // console.log(user)
  // const token = localStorage.getItem('token')

  // useEffect(() => {
  //   axios.get(`/api/users/${getUserId()}`, {
  //     headers: { Authorization: `Bearer ${token}` }
  //   })
  //     .then(resp => {
  //       updateUser(resp.data)
  //       console.log(resp.data)
  //     })
  // }, [])

  return <section className='homepage'>
    <div>
      <h2 className='hp-title'>Poppins</h2>
      <h1 className='hp'>Where Children's Imaginations Run Wild</h1>
    </div>
  </section>
  
}

export default Home