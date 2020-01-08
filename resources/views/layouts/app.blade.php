<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
  <head>
     @include('includes.head')
  </head>

  <body id="app">
    <header>
      @include('includes.header')
    </header>

    <section class="content">
      @yield('content')
    </section>

    <footer>
      @include('includes.footer')
    </footer>

    @yield('modals')
  </body>
</html>