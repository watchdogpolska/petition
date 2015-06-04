var
    fs          = require('fs'), 
    gulp        = require('gulp'), 
    sass        = require('gulp-ruby-sass') ,
    notify      = require("gulp-notify"), 
    bower       = require('gulp-bower'),
    watch       = require('gulp-watch'),
    uglify      = require('gulp-uglifyjs'),
    prefix      = require('gulp-autoprefixer'),
    livereload  = require('gulp-livereload'),
    csslint     = require('gulp-csslint'),
    minifyCss   = require('gulp-minify-css'),
    rename      = require('gulp-rename'),
    sourcemaps  = require('gulp-sourcemaps'),
    json        = JSON.parse(fs.readFileSync('./package.json'));

var config = function(){
    var appName = json.name;
    return {
         'bowerDir'   : './bower_components/' ,
        'assetsDir'  : './' + appName + '/assets',
         'scssDir'    : './' + appName + '/assets/scss',
        'jsAssetDir' : './' + appName + '/assets/js',
        'staticDir'  : './' + appName + '/static',
        'cssDir'     : './' + appName + '/static/css',   
        'jsDir'      : './' + appName + '/static/js',   
        'fontsDir'   : './' + appName + '/static/fonts',   
    }
}();

gulp.task('bower', function() { 
    return bower(config.bowerDir);
});

gulp.task('icons', function() { 
    return gulp.src(
        [
            config.bowerDir + '/fontawesome/fonts/**.*',
            config.bowerDir + '/bootstrap-sass-official/assets/fonts/**/*.*'
        ]) 
         .pipe(gulp.dest(config.fontsDir)); 
});

gulp.task('js', function(){
    // return gulp.src([config.bowerDir + '/jquery/dist/jquery.js']).pipe(uglify('script.js')).pipe(gulp.dest(config.jsDir));
    return gulp.src(
        [
            config.bowerDir + '/jquery/dist/jquery.js',
            config.bowerDir + '/bootstrap-sass-official/assets/javascripts/bootstrap.js',
            config.jsAssetDir + '/*.js'
        ])
        .pipe(uglify('script.js'))
        .pipe(gulp.dest(config.jsDir))
        .pipe(livereload());
});
gulp.task('scss', function() { 
    return sass(
        config.scssDir + '/style.scss',
        {
            style: 'expanded',
             loadPath: [
                  config.bowerDir + '/bootstrap-sass-official/assets/stylesheets',
                 config.bowerDir + '/fontawesome/scss',
                 config.scssDir
            ], 
        //       sourcemap: true,
               trace: true
         })        
        .on('error', function (err) {
            console.error('Error!', err.message);
        })
        //  .pipe(prefix("last 1 version", "> 1%", "ie 8", "ie 7"))
        // .pipe(csslint())
        // .pipe(csslint.reporter())
        // .pipe(sourcemaps.write())
         .pipe(gulp.dest(config.cssDir))
        .pipe(rename({suffix: '.min' }))
        .pipe(minifyCss())
         .pipe(gulp.dest(config.cssDir))
          .pipe(livereload()); 
});

// Rerun the task when a file changes
 gulp.task('watch', function() {
     livereload.listen();
     gulp.watch(config.scssDir + "/**/*.scss", ['scss']); 
     gulp.watch(config.jsAssetDir + "/**/*.js", ['js']); 
});

  gulp.task('default', ['bower', 'icons', 'scss', 'watch']);
