<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
  <head>
     @include('includes.admin.head')
  </head>

  <body class="app header-fixed sidebar-fixed aside-menu-fixed sidebar-lg-show">
    @include('includes.admin.header')
    
    <div class="app-body">
        @include('includes.admin.sidebar')
        <main class="main">
            <div class="container-fluid">
                <div class="animated fadeIn">
                    @include('flash-message')
                    @yield('content')
                </div>
            </div>
        </main>
        @include('includes.admin.rightsidebar')
    </div>

    @include('includes.admin.footer')
  </body>
</html>