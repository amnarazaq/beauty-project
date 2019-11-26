@extends('layouts.app')
@section('content')
<section id="new-header">
    @if (session('status'))
        <div class="alert alert-success" role="alert">
            {{ session('status') }}
        </div>
    @endif

    	<div class="container">
			<div class="row d-flex justify-content-center">
				<div class="banner-image ">
					<img class="" alt="Get the look"src="{{ asset('/images/model.png') }}">
				</div>
				<div class="font-weight-bold pl-2 pr-2" style=" font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;
    font-size: 24px">Get The</div>
				<div class="banner-image-large">
	    			<img alt="Get the look"src="{{ asset('/images/look.PNG') }}">
				</div>
			</div>
			<div class="row d-flex mt-3 ml-2 mr-2">
				<div class="col-md-4">
					<div class=" row">
						<div class="col-md-8">
							<h1>Virtual Makeovers</h1>
							<p class="mt-5" style="color:#f66d9b">Discover our virtual makeover & online makeup tools to help you find the best makeup products.You can find best foundation shade at our website.</p>
						</div>
					</div>	
				</div>
				<div class="col-md-4" >
					<div class="row">
						<div class="col-md-12" id="my_result">
							<img class="w-100" src="{{ asset('/images/camera.jpg') }}">
						</div>
						<div class="col-md-12" id="my-camera"></div>
						<div class="col-md-12">
							<div class="btn-group btn-group-sm d-flex mr-1" role="group" aria-label="button group">
								<button class="btn btn-secondary" type="button" onclick="window.location.href='javascript:void(take_snapshot())'"><i class="fas fa-camera"></i> Snapshot</button>
								<button class="btn btn-secondary" type="button" onclick="cameraOn()"><i class="fas fa-video"></i> Camera</button>
								<button class="btn btn-secondary" type="button"><i class="fas fa-upload"></i> Upload</button>
							</div>
							<!-- <div class="col-sm-5 mt-2"> <a href="javascript:void(take_snapshot())" class="btn btn-primary">Take Snapshot</a></div> -->
						</div>
					</div>
				</div>
				<div class="col-md-4" >
					<div class="row">
						<div class="col-sm-12">
							<img class="w-100" src="{{asset('/images/image.png')}}">
						</div>
					</div>	
				</div>	
			</div>

			
		</div>
		<script language="Javascript">
			function cameraOn() {
				Webcam.set({
					width: 270,
					height: 300,
					dest_width: 640,
					dest_height: 480,
					image_format: 'jpeg',
					jpeg_quality: 90,
					force_flash: false,
					flip_horiz: false,
					fps: 45
				});
		
				Webcam.attach('#my-camera');
				document.getElementById('my_result').style.display = 'none'
				document.getElementById('my-camera').style.display = 'block'
			}
			

			function take_snapshot() {
				Webcam.snap( function(data_uri) {
					document.getElementById('my_result').innerHTML = '<img width="269px" height="300px" src="'+data_uri+'"/>';
				});

				document.getElementById('my_result').style.display = 'block'
				Webcam.reset();
				document.getElementById('my-camera').style.display = 'none'
				// send request to backend to fetch picture information from AI.
			}

		</script>
</section>

@stop

