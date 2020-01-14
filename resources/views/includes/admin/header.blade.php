<header class="app-header navbar">
  <button class="navbar-toggler sidebar-toggler d-lg-none mr-auto" type="button" data-toggle="sidebar-show">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="{{ url('/') }}">
    <img class="navbar-brand-full" src="{{asset('/images/logoG.gif')}}" width="89" height="25" alt="Beauty">
    <img class="navbar-brand-minimized" src="{{asset('/images/minilogo.png')}}" width="30" height="30" alt="CoreUI Logo">
  </a>
  <ul class="nav navbar-nav d-md-down-none">
    <li class="nav-item px-3">
      <a class="nav-link" href="{{ route('admin') }}">Dashboard</a>
    </li>
    <li class="nav-item px-3">
      <a class="nav-link" href="{{ route('users') }}">Users</a>
    </li>
    <li class="nav-item px-3">
      <a class="nav-link" href="{{ route('settings') }}">Settings</a>
    </li>
  </ul>
  <ul class="nav navbar-nav ml-auto mr-4">
    <li class="nav-item dropdown">
      <a class="nav-link" data-toggle="dropdown" href="#">
       <img class="rounded-circle" width="48px" height="48px" src="{{asset('/images/admin1.jpg')}}" alt="{{ Auth::user()->name }}">  
    </a>
    <div class="dropdown-menu dropdown-menu-right">
      <div class="dropdown-header text-center">
        <strong>{{ Auth::user()->name }}</strong>
      </div>
      <a class="dropdown-item" href="{{ route('settings') }}">
        <i class="fa fa-wrench"></i> Settings</a>
      <a class="dropdown-item" href="{{ route('logout') }}"
                      onclick="event.preventDefault();
                                    document.getElementById('logout-form').submit();">
        <i class="fa fa-lock"></i> Logout</a>
        <form id="logout-form" action="{{ route('logout') }}" method="POST" style="display: none;">
                      @csrf
                  </form>
    </div>
    </li>
  </ul>
</header>