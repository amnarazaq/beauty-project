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
			<div class="row d-flex">
				<div class="col-md-7" style="background-color:yellow;">First Column</div>
				<div class="col-md-5" style="background-color:green;">
					<div class="row">
						<div class="col-md-8">
							<div class="row">
								<div class="col-md-12" id="my-camera"></div>
							</div>
							<div class="row justify-content-sm-center">
								<div class="col-sm-5"> <a href="javascript:void(take_snapshot())" class="btn btn-primary">Take Snapshot</a></div>
							</div>
						</div>
						
						<div class="col-md-4">
							<div class="row">
								<div class="col-sm-12" id="my_result"></div>
							</div>
						</div>
					</div>
				</div>	
			</div>
		</div>
		<script language="Javascript">
			
			Webcam.set({
				width: 320,
				height: 240,
				dest_width: 640,
				dest_height: 480,
				image_format: 'jpeg',
				jpeg_quality: 90,
				force_flash: false,
				flip_horiz: true,
				fps: 45
			});
		
			Webcam.attach('#my-camera');

			function take_snapshot() {
				Webcam.snap( function(data_uri) {
					document.getElementById('my_result').innerHTML = '<img class="img-fluid" src="'+data_uri+'"/>';
				});
			}
		</script>
</section>

@stop

