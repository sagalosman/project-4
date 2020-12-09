import React, { useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

const Signup = (props) => {

  const [formData, updateFormData] = useState({
    name: '',
    username: '',
    email: '',
    password: ''
  })

  function handleChange(event) {
    const name = event.target.name
    const value = event.target.value

    const data = {
      ...formData,
      [name]: value
    }
    updateFormData(data)
  }

  function handleSubmit(event) {
    event.preventDefault()

    axios.post('api/signup', formData)
      .then(resp => {
        props.history.push('/login')
      })
  }

  return <div className="session">
    <div className="left">
    </div>
    <form action="" className="log-in" autoComplete="off">
      <h4 className="title"><span>Poppins</span></h4>
      <p className="welcome">Create a new account:</p>

      <div className="field">
        <label className="label">Full Name</label>
        <input
          className="input" 
          type="text"
          onChange={handleChange}
          value={formData.name}
          name="name"
        />
      </div>

      <div className="field">
        <label className="label">Email</label>
        <input
          className="input"
          type="text"
          onChange={handleChange}
          value={formData.email}
          name="email"
        />
      </div>

      <div className="field">
        <label className="label">Password</label>
        <input className="input"
          type="password"
          onChange={handleChange}
          value = {formData.password}
          name="password"
        />
      </div >
      

      <button className="buttonsl" type="submit" onClick={handleSubmit}>Sign Up</button>
      {<Link to='/login' className="discrete">Have an account? Login</Link>}
    </form>
  </div>
}

export default Signup

