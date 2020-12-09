import React from 'react'
import { Switch, Route, BrowserRouter } from 'react-router-dom'



import './styles/sagal.scss'
import './styles/james.scss'
import Home from './components/Home'
import Navbar from './components/Navbar'
import Signup from './components/Signup'
import Login from './components/Login'
import Books from './components/Books'
import SingleBook from './components/SingleBooks'
import SearchBar from './components/SearchBar'

// import User from './components/User'
// import User from './components/UserProfile'

import User from './components/UserProfile'

const App = () => {
  return <BrowserRouter>
    <Navbar/>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/Signup" component={Signup} />
      <Route exact path="/login" component={Login} />
      <Route exact path='/users/:userId' component={User} />
      <Route exact path = "/books" component = {Books} />
      <Route exact path = "/booksearch" component = {SearchBar} />
      <Route exact path = "/user-account" component = {User} />
      <Route exact path = "/books/:bookId" component = {SingleBook} />
      
     
    </Switch>
  </BrowserRouter>
}

export default App