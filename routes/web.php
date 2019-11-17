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
       Route::get('/create', 'Admin\BrandController@create')->name('brands.create');
       Route::post('/create', 'Admin\BrandController@store')->name('brands.store');
       Route::get('/{brand}/edit', 'Admin\BrandController@edit')->name('brands.edit');
       Route::patch('/{brand}/edit', 'Admin\BrandController@update')->name('brands.update');
       Route::delete('/{brand}/delete', 'Admin\BrandController@delete')->name('brands.delete');
       
    });

    Route::group(['prefix' => 'settings'], function() {
         Route::get('/', 'Admin\SettingController@index')->name('settings');
     });

     Route::group(['prefix' => 'categories'], function() {
        Route::get('/', 'Admin\CategoryController@index')->name('categories');
        Route::get('/create', 'Admin\CategoryController@create')->name('categories.create');
        Route::post('/create', 'Admin\CategoryController@store')->name('categories.store');
        Route::get('/{category}/edit', 'Admin\CategoryController@edit')->name('categories.edit');
        Route::patch('/{category}/edit', 'Admin\CategoryController@update')->name('categories.update');
        Route::delete('/{category}/delete', 'Admin\CategoryController@delete')->name('categories.delete');
        
     });

     Route::group(['prefix' => 'products'], function() {
        Route::get('/', 'Admin\ProductController@index')->name('products');
        Route::get('/create', 'Admin\ProductController@create')->name('products.create');
        Route::post('/create', 'Admin\ProductController@store')->name('products.store');
        Route::get('/{category}/edit', 'Admin\ProductController@edit')->name('products.edit');
        Route::patch('/{category}/edit', 'Admin\ProductController@update')->name('products.update');
        Route::delete('/{category}/delete', 'Admin\ProductController@delete')->name('products.delete');
     });

     Route::group(['prefix' => 'users'], function() {
        Route::get('/', 'Admin\UserController@index')->name('users');
     });
});

Auth::routes();