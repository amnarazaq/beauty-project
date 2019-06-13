<section>
	<nav class="navbar navbar-light navbar-expand-lg navbar-fixed-top container fixed-top">
	  <a class="navbar-brand" href="{{ url('/')}}">{{ config('app.name')}}</a>
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
	    <span class="navbar-toggler-icon"></span>
	  </button>

	  <div class="collapse navbar-collapse d-flex-lg justify-content-lg-around" id="navbarSupportedContent">
	    <ul class="navbar-nav m-lg-auto">
	      <li class="nav-item active px-3">
	        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
	      </li>
	      <li class="nav-item px-3">
	        <a class="nav-link" href="#">About</a>
	      </li>
	      <li class="nav-item px-3">
	        <a class="nav-link" href="#">How it Works</a>
	      </li>
	      <li class="nav-item px-3">
	        <a class="nav-link" href="#">Contact Us</a>
	      </li>
	    </ul>
	    <ul class="navbar-nav">
	    	@guest
                <li class="nav-item">
                    <a class="nav-link" href="{{ route('login') }}">{{ __('Login') }}</a>
                </li>
                @if (Route::has('register'))
                    <li class="nav-item">
                        <a class="nav-link" href="{{ route('register') }}">{{ __('Register') }}</a>
                    </li>
                @endif
            @else
                <li class="nav-item dropdown">
                    <a id="navbarDropdown" class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                        {{ Auth::user()->name }} <span class="caret"></span>
                    </a>

                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="{{ route('logout') }}"
                           onclick="event.preventDefault();
                                         document.getElementById('logout-form').submit();">
                            {{ __('Logout') }}
                        </a>

                        <form id="logout-form" action="{{ route('logout') }}" method="POST" style="display: none;">
                            @csrf
                        </form>
                    </div>
                </li>
            @endguest
	    </ul>
	  </div>
	</nav>

</section>