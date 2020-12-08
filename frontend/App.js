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
import BookSearch from './components/BookSearch'
import User from './components/UserProfile'

const App = () => {
  return <BrowserRouter>
    <Navbar/>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route extact path = "/books/booksearch" component = {BookSearch} />
      <Route exact path="/Signup" component={Signup} />
      <Route exact path="/Login" component={Login} />
      <Route exact path='/users/:userId' component={User} />
      <Route exact path = "/books" component = {Books} />
      <Route extact path = "/books/:bookId" component = {SingleBook} />
     
    </Switch>
  </BrowserRouter>
}

export default App