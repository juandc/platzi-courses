import http from 'http'
import React from 'react'
import { renderToString, renderToStaticMarkup } from 'react-dom/server'
import { ServerRouter, createServerRenderContext } from 'react-router'
import { IntlProvider } from 'react-intl'
// Components
import Routes from './routes'
import Layout from './routes/Layout'
import messages from './messages/index.json'

function requestHandler(req, res) {
  const locale = req.headers['accept-language'].indexOf('es') >= 0
    ? 'es'
    : 'en'
  const context = createServerRenderContext()
  const result = context.getResult()

  let html = renderToString(
    <IntlProvider locale={locale} messages={messages[locale]}>
      <ServerRouter location={req.url} context={context} >
        <Routes />
      </ServerRouter>
    </IntlProvider>,
  )

  res.setHeader('Content-Type', 'text/html')

  if (result.redirect) {
    res.writeHead(301, {
      Location: result.redirect.pathname,
    })
    res.end()
  }
  if (result.missed) {
    res.writeHead(404)
    html = renderToString(
      <IntlProvider locale={locale} messages={messages[locale]}>
        <ServerRouter location={req.url} context={context} >
          <Routes />
        </ServerRouter>
      </IntlProvider>,
    )
  }

  res.write(
    renderToStaticMarkup(
      <Layout
        title="React - Backend For Frontend"
        content={html}
      />,
    ),
  )
  res.end()
}

const server = http.createServer(requestHandler)
server.listen(3000)
