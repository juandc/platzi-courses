import React, { Component } from 'react'
// import { Link } from 'react-router'
// Components
import Loading from '../components/Loading'
import Comment from '../components/Comment'
import PostBody from './Post'
// API
import api from '../../api'

class Post extends Component {
  constructor(props) {
    super(props)

    this.state = {
      loading: true,
      user: {},
      post: {},
      comments: [],
    }
  }
  componentDidMount() { this.initialFetch() }
  async initialFetch() {
    const [
      post,
      comments,
    ] = await Promise.all([
      api.posts.getSingle(this.props.params.id),
      api.posts.getComments(this.props.params.id),
    ])

    const user = await api.users.getSingle(post.userId)

    this.setState({
      loading: false,
      post,
      user,
      comments,
    })
  }
  render() {
    if (this.state.loading) {
      return <Loading />
    }
    return (
      <section name="Post">
        <PostBody
          user={this.state.user}
          comments={this.state.comments}
          {...this.state.post}
        />
        <div>
          {this.state.comments.map(comment => (
            <Comment key={comment.id} {...comment} />
          ))}
        </div>
      </section>
    )
  }
}

Post.propTypes = {
  params: React.PropTypes.shape({
    id: React.PropTypes.string,
  }),
}

export default Post
