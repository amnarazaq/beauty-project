<header class="app-header navbar">
  <button class="navbar-toggler sidebar-toggler d-lg-none mr-auto" type="button" data-toggle="sidebar-show">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="#">
    <img class="navbar-brand-full" src="{{asset('/images/Logo.jpg')}}" width="89" height="25" alt="Beauty">
    <img class="navbar-brand-minimized" src="{{asset('/images/Logo.jpg')}}" width="30" height="30" alt="CoreUI Logo">
  </a>
  <button class="navbar-toggler sidebar-toggler d-md-down-none" type="button" data-toggle="sidebar-lg-show">
    <span class="navbar-toggler-icon"></span>
  </button>
  <ul class="nav navbar-nav d-md-down-none">
    <li class="nav-item px-3">
      <a class="nav-link" href="#">Dashboard</a>
    </li>
    <li class="nav-item px-3">
      <a class="nav-link" href="#">Users</a>
    </li>
    <li class="nav-item px-3">
      <a class="nav-link" href="#">Settings</a>
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
      <a class="dropdown-item" href="#">
        <i class="fa fa-user"></i> Profile</a>
      <a class="dropdown-item" href="#">
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