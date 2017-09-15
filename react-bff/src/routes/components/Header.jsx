import React from 'react'
import { Link } from 'react-router'
// Styles
import styles from '../../styles/style.css'

function Header(/* props */) {
  return (
    <header className={styles.header} >
      <h1>React BFF</h1>
      <nav role="navigation">
        <Link to="/" activeClassName={styles.active} activeOnlyWhenExact>
          Home
        </Link>
      </nav>
    </header>
  )
}

export default Header
