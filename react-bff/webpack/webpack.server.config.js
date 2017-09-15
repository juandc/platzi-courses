const ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  entry: './src/server.jsx',
  output: {
    filename: 'index.js',
    path: './build/server',
  },
  module: {
    preLoaders: [
      {
        test: /\.jsx?$/,
        loader: 'eslint',
        exclude: /(node_modules)/,
      },
    ],
    loaders: [
      { test: /\.json$/, loader: 'json' },
      {
        test: /\.jsx?$/,
        loader: 'babel',
        exclude: /(node_modules)/,
        query: { presets: ['latest-minimal', 'react'] },
      },
      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract('style', 'css?modules!stylus-loader'),
      },
    ],
  },
  resolve: { extensions: ['', '.js', '.jsx', '.json'] },
  target: 'node',
  plugins: [
    new ExtractTextPlugin('../static/style.css'),
  ],
}
