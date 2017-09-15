import React, { Component, PropTypes } from 'react'
import { Link } from 'react-router'
import { FormattedMessage } from 'react-intl'
// API
import api from '../../api'

class PostBody extends Component {
  constructor(props) {
    super(props)

    this.state = {
      loading: true,
      user: props.user || null,
      comments: props.comments || null,
    }
  }
  componentDidMount() { this.initialFetch() }
  async initialFetch() {
    if (!!this.state.user && !!this.state.comments) {
      return this.setState({ loading: false })
    }
    const [
      user,
      comments,
    ] = await Promise.all([
      !this.state.user
        ? api.users.getSingle(this.props.userId)
        : Promise.resolve(null),
      !this.state.comments
        ? api.posts.getComments(this.props.id)
        : Promise.resolve(null),
    ])

    return this.setState({
      loading: false,
      user: user || this.state.user,
      comments: comments || this.state.comments,
    })
  }
  render() {
    return (
      <article id={`post-${this.props.id}`}>
        <Link to={`/post/${this.props.id}`}>
          <h2>{this.props.title}</h2>
        </Link>
        <p>{this.props.body}</p>
        {!this.state.loading && (
          <div>
            <Link to={`/user/${this.state.user.id}`}>
              {this.state.user.name}
            </Link>
            <FormattedMessage
              id="post.comment.length"
              values={{
                comments: this.state.comments.length,
              }}
            />
            <Link to={`/post/${this.props.id}`}>
              <FormattedMessage id="post.readMore" />
            </Link>
          </div>
        )}
      </article>
    )
  }
}

PostBody.propTypes = {
  body: PropTypes.string,
  comments: PropTypes.arrayOf(
    React.PropTypes.object,
  ),
  id: PropTypes.number,
  title: PropTypes.string,
  user: PropTypes.shape({
    name: React.PropTypes.string,
  }),
  userId: PropTypes.number,
}

export default PostBody
