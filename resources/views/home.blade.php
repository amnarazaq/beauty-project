@extends('layouts.app')
@section('content')
<section id="new-header" style="margin-top: 100px">
    @if (session('status'))
        <div class="alert alert-success" role="alert">
            {{ session('status') }}
        </div>
    @endif

    	<div class=" container img-fluid">
			<div class="row d-flex justify-content-center">
				<div class="banner-image ">
					<img class="" alt="Get the look"src="{{asset('/images/model.png')}}">
				</div>
				<div class="font-weight-bold pl-2 pr-2" style=" font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;
    font-size: 24px">Get The</div>
				<div class="banner-image--large">
	    			<img class="" alt="Get the look"src="{{asset('/images/look.PNG')}}">
				</div>
			</div>
		</div>
		
</section>
<section id="new-body">
</section>

@stop

