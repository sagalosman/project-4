import React, { useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

const Login = (props) => {

  const [formData, updateFormData] = useState({
    email: '',
    password: ''
  })
  console.log(props)
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
    axios.post('/api/login', formData)
      .then(resp => {
        localStorage.setItem('token', resp.data.token)
        localStorage.setItem('username', resp.data.username)
        props.history.push('/')
      })
  }

  return <div className="session">
    <div className="left">
    </div>
    <form action="" className="log-in" autoComplete="off">
      <h4 className="title"><span>Poppins</span></h4>
      <p className="welcome">Welcome back! Log in to your account:</p>
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
          value={formData.password}
          name="password"
        />
      </div >

      <button className="buttonsl" type="submit" onClick={handleSubmit}>Log in</button>
      <Link to="/signup" className="discrete">Not registered? Sign up</Link>
    </form>
  </div>
}

export default Login