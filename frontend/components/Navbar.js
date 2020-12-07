import React from 'react'
import { Link } from 'react-router-dom'
// import Logo from './images/open-book.png'

const Navbar = () => {
  return <section>
  <nav className="nav">
    <div className='ul' >
            <Link className='a'className="li"  to="/Signup">Signup</Link>
            <Link className='a'className="li"  to="/Login">Login</Link>
            <Link className='a'className="li"   to="/">Home</Link>
            </div>
  </nav>
  </section>
}

export default Navbar