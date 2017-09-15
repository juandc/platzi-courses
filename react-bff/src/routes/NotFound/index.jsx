import React from 'react'
import { Link } from 'react-router'
import { FormattedMessage } from 'react-intl'

function NotFound(/* props */) {
  return (
    <section name="NotFound">
      <FormattedMessage id="notFound.msg" tagName="h3" />
      <Link to="/"><FormattedMessage id="notFound.link" /></Link>
    </section>
  )
}

export default NotFound
