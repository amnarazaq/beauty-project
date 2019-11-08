const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */


 mix.js([
	'resources/js/app.js',
	'resources/js/custom.js'
	], 'public/js')
    .sass('resources/sass/app.scss', 'public/css');

//admin coreui files.
mix.combine([
	'node_modules/@coreui/coreui/dist/js/coreui.js',
	'node_modules/@coreui/coreui-plugin-chartjs-custom-tooltips/dist/js/custom-tooltips.js'
	], 'public/js/coreui.js');

mix.combine([
		'node_modules/popper.js/dist/umd/popper.js',
		'node_modules/pace-progress/pace.js',
		'node_modules/perfect-scrollbar/dist/perfect-scrollbar.js'
	], 'public/js/coreui-required.js');
	
mix.js('node_modules/chart.js/dist/Chart.js', 'public/js/Chart.js');

mix.combine([
	'resources/css/style.css'
	], 'public/css/coreui-icons.css');


//Copy images.
mix.copyDirectory('resources/images', 'public/images');