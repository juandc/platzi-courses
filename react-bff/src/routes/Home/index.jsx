import React, { Component } from 'react'
// import { Link } from 'react-router'
// Api
import api from '../../api'
// Components
import PostBody from '../Post/Post'
import Loading from '../components/Loading'

class Home extends Component {
  constructor(props) {
    super(props)

    this.state = {
      page: 1,
      posts: [],
      loading: true,
    }

    this.handleScroll = this.handleScroll.bind(this)
  }
  componentDidMount() {
    this.initialFetch()
    window.addEventListener('scroll', this.handleScroll)
  }
  componentWillUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  }
  handleScroll() {
    if (this.state.loading) return null

    const scrolled = window.scrollY
    const viewportHeight = window.innerHeight
    const fullHeight = document.body.clientHeight

    if (!(scrolled + viewportHeight + 50 >= fullHeight)) return null

    return this.setState({ loading: true }, async () => {
      try {
        const posts = await api.posts.getList(this.state.page)
        this.setState({
          posts: this.state.posts.concat(posts),
          page: this.state.page + 1,
          loading: false,
        })
      } catch (error) {
        this.setState({ loading: false })
      }
    })
  }
  async initialFetch() {
    const posts = await api.posts.getList(this.state.page)
    this.setState({
      posts,
      page: this.state.page + 1,
      loading: false,
    })
  }
  render() {
    return (
      <section name="Home">
        <article>
          {this.state.posts.map(post => <PostBody key={post.id} {...post} />)}
          {this.state.loading && (
            <Loading />
          )}
        </article>
      </section>
    )
  }
}

export default Home
