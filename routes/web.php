<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('pages.home');
});

Route::get('/home', 'HomeController@index')->name('home');

Route::group(['prefix' => 'admin', 'middleware' => ['auth', 'role:admin']], function() {
    Route::get('/', 'Admin\AdminController@index')->name('admin');

    Route::group(['prefix' => 'brands'], function() {
       Route::get('/', 'Admin\BrandController@index')->name('brands');
    });

    Route::group(['prefix' => 'settings'], function() {
        Route::get('/', 'Admin\SettingController@index')->name('settings');
     });

     Route::group(['prefix' => 'categories'], function() {
        Route::get('/', 'Admin\CategoryController@index')->name('categories');
     });

     Route::group(['prefix' => 'products'], function() {
        Route::get('/', 'Admin\ProductController@index')->name('products');
     });

     Route::group(['prefix' => 'users'], function() {
        Route::get('/', 'Admin\UserController@index')->name('users');
     });
});

Auth::routes();