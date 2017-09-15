import React from 'react'
import { render } from 'react-dom'
import { BrowserRouter } from 'react-router'
import { addLocaleData, IntlProvider } from 'react-intl'
import en from 'react-intl/locale-data/en'
import es from 'react-intl/locale-data/es'
// Components
import Routes from './routes'
import messages from './messages/index.json'

addLocaleData([...en, ...es])

const locale = navigator.languages.indexOf('es') >= 0 ? 'es' : 'en'

render(
  <IntlProvider locale={locale} messages={messages[locale]}>
    <BrowserRouter>
      <Routes />
    </BrowserRouter>
  </IntlProvider>,
  document.getElementById('App'),
)
