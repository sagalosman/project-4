import React from 'react'
import { Link } from 'react-router-dom'
// import Logo from './images/open-book.png'

const Navbar = () => {
  return <section>
  <nav className="nav1">
    {/* <img src={logo} alt="My logo" /> */}
    <div className='ul1' >
      <Link className='a1'className="li1"  to="/Signup">Signup</Link>
      <Link className='a1'className="li1"  to="/Login">Login</Link>
      <Link className='a1'className='li1'  to = "/books/booksearch"> Search Books</Link>
      <Link className='a1'className="li1"   to = "/books">Books</Link>
      <Link className='a1'className="li1"   to="/">Home</Link>
      <Link className='a1'className='li1'  to = "/books/:bookId"></Link>
    </div>
  </nav>
  </section>
}

export default Navbar