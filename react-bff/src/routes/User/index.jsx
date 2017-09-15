import React, { Component } from 'react'
import { FormattedMessage } from 'react-intl'
// import { Link } from 'react-router'
// API
import api from '../../api'
// Components
import PostBody from '../Post/Post'
import Loading from '../components/Loading'

class User extends Component {
  constructor(props) {
    super(props)

    this.state = {
      user: {},
      posts: [],
      loading: true,
    }
  }
  componentDidMount() { this.initialFetch() }
  async initialFetch() {
    const [
      user,
      posts,
    ] = await Promise.all([
      api.users.getSingle(this.props.params.id),
      api.users.getPosts(this.props.params.id),
    ])
    this.setState({
      user,
      posts,
      loading: false,
    })
  }
  render() {
    if (this.state.loading) {
      return <Loading />
    }
    return (
      <section name="User">
        <FormattedMessage
          id="user.title"
          tagName="h2"
          values={{
            name: this.state.user.name,
          }}
        />
        <fieldset>
          <FormattedMessage id="user.info" tagName="legend" />
          <input type="email" value={this.state.user.email} disabled />
          <br />
          <a href={`//${this.state.user.website}`} target="_blanck" rel="nofollow">
            <FormattedMessage id="user.website" />
          </a>
        </fieldset>
        {this.state.user.address && (
          <fieldset>
            <FormattedMessage id="user.address" tagName="legend" />
            <address>
              {this.state.user.address.street} <br />
              {this.state.user.address.suite} <br />
              {this.state.user.address.city} <br />
              {this.state.user.address.zipcode} <br />
            </address>
          </fieldset>
        )}
        <article>
          { this.state.posts.map(post => (
            <PostBody
              key={post.id}
              user={this.state.user}
              {...post}
            />
          )) }
        </article>
      </section>
    )
  }
}

User.propTypes = {
  params: React.PropTypes.shape({
    id: React.PropTypes.string,
  }),
}

export default User
