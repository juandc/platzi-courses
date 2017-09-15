var atImport    = require('postcss-import')
var bem         = require('postcss-bem')
var browserSync = require('browser-sync').create()
var cssnested   = require('postcss-nested')
var cssnext     = require('postcss-cssnext')
var csswring    = require('csswring')
var gulp        = require('gulp')
var lost        = require('lost')
var mixins      = require('postcss-mixins')
var mqpacker    = require('css-mqpacker')
var postcss     = require('gulp-postcss')
var rename      = require('gulp-rename')
var rucksack    = require('rucksack-css')

var processors = [
  atImport(),
  bem,
  mixins(),
  cssnested,
  lost(),
  rucksack(),
  cssnext({ browsers: ['> 5%'] }),
  mqpacker({sort:true})
]

gulp.task('server', function () {
  browserSync.init({
    server: {
      baseDir: './public'
    }
  })
})

gulp.task('styles', function () {
  return gulp.src('./src/index.css')
    .pipe(postcss(processors))
    .pipe(rename("style.css"))
    .pipe(gulp.dest('./public/css'))
    .pipe(browserSync.stream())
})

gulp.task('minStyles', function () {
  return gulp.src('./public/css/style.css')
    .pipe(postcss([csswring()]))
    .pipe(rename("style.min.css"))
    .pipe(gulp.dest('./public/css'))
    .pipe(browserSync.stream())
})

gulp.task('watch', function () {
  gulp.watch('./src/*.css', ['styles', 'minStyles'])
  gulp.watch('./public/*.html').on('change', browserSync.reload)
})

gulp.task('default', ['watch', 'server'])
