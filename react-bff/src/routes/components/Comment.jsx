import React from 'react'
import { FormattedHTMLMessage } from 'react-intl'

function Comment(props) {
  return (
    <article id={`comment-${props.id}`}>
      <div>
        <FormattedHTMLMessage
          id="comment.author"
          values={{
            name: props.name,
            email: props.email,
          }}
        />
      </div>
      <p>{props.body}</p>
    </article>
  )
}

Comment.propTypes = {
  body: React.PropTypes.string,
  email: React.PropTypes.string,
  id: React.PropTypes.number,
  name: React.PropTypes.string,
}

export default Comment
