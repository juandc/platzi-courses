import React from 'react'
import {
  Match,
  Miss,
} from 'react-router'
// Components
import Home from './Home'
import Post from './Post'
import User from './User'
import NotFound from './NotFound'
import Header from './components/Header'

function Routes() {
  return (
    <main role="application">
      <Header />
      <Match
        pattern="/"
        exactly
        component={Home}
      />
      <Match
        pattern="/post/:id"
        exactly
        component={Post}
      />
      <Match
        pattern="/user/:id"
        exactly
        component={User}
      />
      <Miss component={NotFound} />
    </main>
  )
}

export default Routes
