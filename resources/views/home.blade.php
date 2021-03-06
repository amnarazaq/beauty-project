@extends('layouts.app')
@section('content')
<section id="new-header">
    @if (session('status'))
        <div class="alert alert-success" role="alert">
            {{ session('status') }}
        </div>
    @endif
		<div class="container">
			<form  enctype="multipart/form-data" method="POST" id="beautyForm" action="{{ route('show-beauty') }}">
			@csrf
				<div class="row d-flex justify-content-center" style="margin-top:85px">
					<div class="banner-image ">
						<img class="" alt="Get the look"src="{{ asset('/images/model.png') }}">
					</div>
					<div 
						class="font-weight-bold pl-2 pr-2"
						style="font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;font-size: 24px"
					>
						Get The
					</div>
					<div class="banner-image-large">
						<img alt="Get the look"src="{{ asset('/images/look.png') }}">
					</div>
				</div>
				<div class="row d-flex justify-content-md-between justify-content-sm-center flex-md-wrap mt-3 ml-2 mr-2">
					<div style="width: 300px;">
						<div class=" row">
							<div class="col-md-8">
								<div class="font-weight-bold pl-2 pr-2" style=" font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;
									font-size: 32px">Virtual</div>
								<div class="banner-image-large">
									<img alt="makeovers"src="{{ asset('/images/makeovers.png') }}">
								</div>
								<p class="mt-3 pl-2">Discover our virtual makeover & online makeup tools to help you find the best makeup products.You can find best foundation shade at our website.</p>
							</div>
						</div>	
					</div>
					<div style="width: 270px;">
						<div class="row">
							<div class="col-md-12" id="my_result">
								<img class="w-100" src="{{ asset('/images/camera.jpg') }}">
							</div>
							<div class="col-md-12" id="my-camera"></div>
							<div class="col-md-12">
								<div class="btn-group btn-group-sm d-flex mr-1" role="group" aria-label="button group">
									<button class="btn btn-secondary btn-cam" type="button" onclick="window.location.href='javascript:void(take_snapshot())'"><i class="fas fa-camera"></i> Snapshot</button>
									<button class="btn btn-secondary btn-cam" type="button" onclick="cameraOn()"><i class="fas fa-video"></i> Camera</button>
									<input type="file" name="picture" capture="camera" accept="image/*" id="uploadImageInput" class="btn btn-secondary btn-cam d-none">
									<button class="btn btn-secondary btn-cam" type="button" onclick="uploadClick()"><i class="fas fa-upload"></i> Upload</button>
								</div>
							</div>
						</div>
					</div>
					<div style="width: 300px;">
						<div class="row">
							<div class="col-sm-12">
								<img class="w-100" src="{{asset('/images/image.png')}}">
							</div>
						</div>	
					</div>	
				</div>
				<div class="row mt-4">
					<div class="col-sm-12 col-md-6">
						<div class="row">
							<div class="col-sm-12 d-flex">
								<div class="font-weight-bold pl-2 pr-2" style=" font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;
									font-size: 28px; padding-top:5px">Select</div>
								<div class="banner-image-large">
									<img alt="look2"src="{{ asset('/images/look2.png') }}">
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="row">	
					<div class="col-sm-12 col-md-5 ml-2 mt-2">
						<div class="d-flex justify-content-between">
							<div class="radio">
								<label class="lb-check">
									<input type="radio" name="lookChoice" class="choice" value="bridal">
									<span class="cr text-center">
										<span>Bridal</span>
									</span>
								</label>
							</div>
							<div class="radio">
								<label class="lb-check">
									<input type="radio" name="lookChoice" class="choice" value="casual" checked>
									<span class="cr text-center">
										<span>Casual</span>
									</span>
								</label>
							</div>
							<div class="radio">
								<label class="lb-check">
									<input type="radio" name="lookChoice" class="choice" value="party">
									<span class="cr text-center">
										<span>Party</span>
									</span>
								</label>
							</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="col-sm-12 col-md-4 mt-2">
						<div class="row">
							<div class="col-sm-12 d-flex">
								<div class="font-weight-bold pl-2 pr-2" style=" font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;
									font-size: 28px; padding-top:4px">Select Dress</div>
								<div class="banner-image-large">
									<img alt="color" src="{{ asset('/images/color.png') }}">
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="col-sm-12 col-md-4 pb-3 ml-2 mt-2">
						<input type="color" name="dressColor" value="#FF1493" style="width:100%;">
					</div>
				</div>
				<div class="d-flex justify-content-center mt-2">
					<button class="btn btn-cam" type="submit" ><i class="fas fa-grin-hearts"></i> <b>Show Beauty</b></button>
				</div>
			</form>
		</div>
</section>

@stop
@section('custom-js')
<script type="text/javascript">
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#my_result').html('<img width="269px" height="300px" src="'+ e.target.result+'"/>')
            }
			reader.readAsDataURL(input.files[0]);
        }
    }
	
	$("#uploadImageInput").change(function() {
        readURL(this);
	});

	function uploadClick() {
		document.getElementById('my_result').style.display = 'block'
		Webcam.reset();
		document.getElementById('my-camera').style.display = 'none'
		$('#uploadImageInput').trigger('click');
	}
	
	function cameraOn() {
		Webcam.set({
			width: 269,
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
		$('#cameraImage').remove();
	}		

	function take_snapshot() {
		Webcam.snap( function(data_uri) {
			document.getElementById('my_result').innerHTML = '<img width="269px" height="300px" src="'+data_uri+'"/>';
			form = document.getElementById('beautyForm');
			$('#beautyForm').append($('<input type="hidden" id="cameraImage" name="cameraImage" value="'+data_uri+'">'));
		});

		document.getElementById('my_result').style.display = 'block'
		Webcam.reset();
		document.getElementById('my-camera').style.display = 'none'
	}
</script>
@stop

