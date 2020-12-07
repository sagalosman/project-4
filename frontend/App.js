import React from 'react'
import { Switch, Route, BrowserRouter } from 'react-router-dom'



import './styles/sagal.scss'
import Home from './components/Home'
import Navbar from './components/Navbar'
import Signup from './components/Signup'
import Login from './components/Login'


const App = () => {
  return <BrowserRouter>
    <Navbar/>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/Signup" component={Signup} />
      <Route exact path="/Login" component={Login} />
    </Switch>
  </BrowserRouter>
}


export default App