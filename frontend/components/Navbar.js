import React from 'react'
import { Link } from 'react-router-dom'
// import Logo from './images/open-book.png'

const Navbar = () => {
  return <nav className="nav">
    {/* <img src={logo} alt="My logo" /> */}
    <div className='ul' >
      <Link className='a'className="li"  to="/Signup">Signup</Link>
      <Link className='a'className="li"  to="/Login">Login</Link>
      <Link className='a'className="li"   to="/">Home</Link>
      <Link className='a'className="li"   to = "/books">Books</Link>
      <Link className='a'className='li'  to = "/books/:bookId"></Link>
      {/* <Link className='a'className='li'  to = "/searchPage"> Search Books</Link> */}
    </div>
  </nav>
}

export default Navbar