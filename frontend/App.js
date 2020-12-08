import React from 'react'
import { Switch, Route, BrowserRouter } from 'react-router-dom'



import './styles/sagal.scss'
import Home from './components/Home'
import Navbar from './components/Navbar'
import Signup from './components/Signup'
import Login from './components/Login'
// import User from './components/User'
import Books from './components/Books'
import SingleBook from './components/SingleBooks'
import SearchBar from './components/SearchBar'

// import User from './components/User'
// import User from './components/UserProfile'

const App = () => {
  return <BrowserRouter>
    <Navbar/>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path = "/booksearch" component = {SearchBar} />

      <Route exact path="/Signup" component={Signup} />
      <Route exact path="/Login" component={Login} />
      {/* <Route exact path='/users/:userId' component={UserProfile} /> */}
      <Route exact path = "/books" component = {Books} />
      <Route exact path = "/books/:bookId" component = {SingleBook} />
     
      {/* <Route exact path='/users/:userId' component={User} /> */}
    </Switch>
  </BrowserRouter>
}

export default App