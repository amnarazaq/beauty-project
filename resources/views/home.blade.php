@extends('layouts.app')
@section('content')
<div class="container  mt-5 text-center">
    @if (session('status'))
      <div class="alert alert-success" role="alert">
            {{ session('status') }}
       </div>
     @endif
     You are logged in!
 </div>
        </div>
    </div>
</div>
@stop

