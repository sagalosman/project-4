import React from 'react'
import { Link } from 'react-router-dom'
// import Logo from './images/open-book.png'

const Navbar = () => {
  return <section>
    <nav className="nav">
      <div>
        {/* <a className="navicon" href="/">
          <img src="https://i.imgur.com/dlKZbjY.png" alt="Poppins" width='50px' />

        </a> */}
        <div className='ul' >
          <Link className='a' className="li" to="/Signup">Signup</Link>
          <Link className='a' className="li" to="/Login">Login</Link>
          <Link className='a' className="li" to="/books">Books</Link>
          <Link className='a' className="li" to="/">Home</Link>
          <Link className='a' className='li' to="/books/:bookId"></Link>
          <Link className='a' className='li' to="/books/booksearch"> Search Books</Link>
        </div>
      </div>
    </nav>
  </section>
}

export default Navbar