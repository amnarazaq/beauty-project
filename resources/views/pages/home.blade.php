@extends('layouts.app')
@section('main-banner')
<section id="banner">
<div id="slider">
	<!-- Navigation -->
  <div class="carousel slide carousel-fade" data-ride="carousel">
    <div class="carousel-inner" role="listbox">
      <!-- Slide One - Set the background image for this slide in the line below -->
		<div class="carousel-item active" style="background-image:url('/images/slider-image/slide1.jpg')">
			<div class="row d-flex"style="margin-top: 250px;">
				<div class="col-sm-6">
					<div class="title d-flex justify-content-center">
						<h1  style="font-family:  Arial Black">Welcome</h1>
					</div>
					<div class="description d-flex justify-content-center" style="font-family:  Georgia;">
						<h2>To a Glamorous Beauty</h2>
					</div>
					<div class="d-flex justify-content-center">
						@auth 
							<a href="{{ route('home') }}" class="btn btn-cam"><b>Try Virtual Look</b></a>
						@endauth
						@guest
						<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
							Try Virtual Look
						</button>
						@endguest
					</div>
				</div>
			</div>
		</div>
     <!-- Slide Two - Set the background image for this slide in the line below -->
	<div class="carousel-item"style="background-image:url('/images/slider-image/slide2.jpg')">
		<div class="row d-flex"style="margin-top: 250px;">
			<div class="col-sm-6 offset-md-6 float-sm-right">
				<div class="title d-flex justify-content-center">
					<h1  style="font-family:  Arial Black">Staying in</h1>
				</div>
				<div class="description d-flex justify-content-center" style="font-family:  Georgia;">
					<h2>style forever</h2>
				</div>
				<div class="d-flex justify-content-center">
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam"><b>Try Virtual Look</b></a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
						Try Virtual Look
					</button>
					@endguest
				</div>
			</div>
		</div>
    </div>
       <!-- Slide Three - Set the background image for this slide in the line below -->
    <div class="carousel-item"style="background-image:url('/images/slider-image/slide3.jpg')">
	  <div class="row d-flex"style="margin-top: 250px;">
			<div class="col-sm-6">
				<div class="title d-flex justify-content-center">
					<h1  style="font-family:  Arial Black;">Creativity</h1>
				</div>
				<div class="description d-flex justify-content-center text-center" style="font-family:  Georgia;">
					<h2>is your best makeup skill, don't be afraid to experiment</h2>
				</div>
				<div class="d-flex justify-content-center">
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam"><b>Try Virtual Look</b></a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
						Try Virtual Look
					</button>
					@endguest
				</div>
			</div>
		</div>
	</div>
	  <!-- Slide four - Set the background image for this slide in the line below -->
	<div class="carousel-item"style="background-image:url('/images/slider-image/slide4.jpg')">
		<div class="row d-flex"style="margin-top: 250px;">
			<div class="col-sm-6 offset-md-6 float-sm-right">
				<div class="title d-flex justify-content-center">
					<h1  style="font-family:  Arial Black">The Future</h1>
				</div>
				<div class="description d-flex justify-content-center" style="font-family:  Georgia;color:white">
					<h2>of beauty is here</h2>
				</div>
				<div class="d-flex justify-content-center">
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam"><b>Try Virtual Look</b></a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
						Try Virtual Look
					</button>
					@endguest
				</div>
			</div>
		</div>
	</div>
	 <!-- Slide five - Set the background image for this slide in the line below -->
    <div class="carousel-item"style="background-image:url('/images/slider-image/slide5.jpg')">
	    <div class="row d-flex"style="margin-top: 250px;">
			<div class="col-sm-6">
				<div class="title d-flex justify-content-center">
					<h1  style="font-family:  Arial Black; color:white">Complete looks</h1>
				</div>
				<div class="description d-flex justify-content-center text-center" style="font-family:  Georgia; color:white">
					<h2>combined with multiple products to create amazing makeovers</h2>
				</div>
				<div class="d-flex justify-content-center">
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam"><b>Try Virtual Look</b></a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
						Try Virtual Look
					</button>
					@endguest
				</div>
			</div>
		</div>
	</div>
	<!--   Slide six - Set the background image for this slide in the line below -->
    <div class="carousel-item"style="background-image:url('/images/slider-image/slide6.jpg')">
	  <div class="row d-flex"style="margin-top: 250px;">
			<div class="col-sm-6 offset-md-6 float-sm-right">
				<div class="title d-flex justify-content-center">
					<h1  style="font-family:  Arial Black">Staying in</h1>
				</div>
				<div class="description d-flex justify-content-center" style="font-family:  Georgia;">
					<h2>style forever</h2>
				</div>
				<div class="d-flex justify-content-center">
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam" ><b>Try Virtual Look</b></a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal" style="background-color:#C8AD98">
						Try Virtual Look
					</button>
					@endguest
				</div>
			</div>
		</div>
	</div>
	 <!--  Slide seven - Set the background image for this slide in the line below -->
    <div class="carousel-item"style="background-image:url('/images/slider-image/slide7.jpg')">
		<div class="row d-flex"style="margin-top: 250px;">
			<div class="col-sm-6">
				<div class="title d-flex justify-content-center">
					<h1  style="font-family:  Arial Black; color:white">Tutorial</h1>
				</div>
				<div class="description d-flex justify-content-center" style="font-family:  Georgia; color:white">
					<h2>To get amazing look</h2>
				</div>
				<div class="d-flex justify-content-center">
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam"><b>Try Virtual Look</b></a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
						Try Virtual Look
					</button>
					@endguest
				</div>
			</div>
		</div>
    </div>
    </div>
    </div>
</div>
</section>
@stop
@section('content')
<section id="about-us">
	<div class="container py-5">
		<div class="row">
			<div class="col-sm-12 text-center"><strong><h2 style="font-family:  Arial Black">About Us</h2></strong></div>
		</div>
		<div class="row">
			<div class="col-sm-12 offset-lg-5 col-lg-7 mt-3"style="font-family:  Georgia">
				<h5>Whether you want a new look for a special occasion or you want to do regular makeup this website will help you in choosing a look which suits you perfect in few minutes. This website is for ease of customers to decide which look will suits on them and which product is suitable for their skin in less time.</h5>
			</div>
		</div>
	</div>
</section>
<section id="how-it-works">
	<div class="container py-5">
		<div class="row">
			<div class="col-sm-12 text-left ml-5"><strong><h2  style="font-family:  Arial Black">How it Works</h2></strong></div>
		</div>
		<div class="row d-flex justify-content-center">
			<div class="col-sm-3 justify-content-center">
				<div>
					<img class="rounded-circle mx-auto d-block" width="130px" height="130px" src="https://beauty-project.site/images/image.png" alt="">
				</div>
				<div class="text-center">
					<p><b>FACIAL TECHNOLOGY</b></p>
				</div>
			</div>
			<div class="col-sm-3 justify-content-center">
				<div>
					<img class="rounded-circle mx-auto d-block" width="130px" height="130px" src="https://beauty-project.site/images/image.png" alt="">
				</div>
				<div class="text-center">
					<p><b>MAKEUP VERSATILITY</b></p>
				</div>
			</div>
			<div class="col-sm-3 justify-content-center">
				<div>
					<img class="rounded-circle mx-auto d-block" width="130px" height="130px" src="https://beauty-project.site/images/image.png" alt="">
				</div>
				<div class="text-center">
					<p><b>FULL MAKEOVERS</b></p>
				</div>
			</div>
			<div class="col-sm-3 justify-content-center">
				<div>
					<img class="rounded-circle mx-auto d-block" width="130px" height="130px" src="https://beauty-project.site/images/image.png" alt="">
				</div>
				<div class="text-center">
					<p style="margin-bottom: 0PX"><b>COMPARE BEFORE AND</b></p>
					<span><b>AFTER</b></span>
				</div>
			</div>
		</div>
	</div>
</section>
<section id="contact-us">
<div class="container py-5">
	<div class="row">
        <div class="col-md-6">
        	<div class="well well-sm">
          		<form class="form-horizontal" action="" method="post">
          			<fieldset style="background-color:white; border-radius:5px">
						<div class="contact-title">
							<div class="col-sm-12 text-center form-title pt-4"><span><strong><h2  style="font-family: Arial Black">
								Contact Us</h2></strong></span>
								<span>Feel free to drop us a line below</span>
							</div>
						</div>
           				 <!-- Name input-->
            			<div class="row form-group m-2">
             				<label class="col-md-3 control-label" for="contactName">Name</label>
              				<div class="col-md-9">
                				<input id="contactName" name="contactName" type="text" placeholder="Your name" class="form-control">
              				</div>
						</div>
						<!-- Email input-->
						<div class="row form-group m-2">
							<label class="col-md-3 control-label" for="contactEmail">E-mail</label>
							<div class="col-md-9">
								<input id="contactEmail" name="contactEmail" type="text" placeholder="Your email" class="form-control">
							</div>
						</div>
						<!-- Message body -->
						<div class="row form-group m-2">
							<label class="col-md-3 control-label" for="contactMessage">Message</label>
							<div class="col-md-9">
								<textarea class="form-control" id="contactMessage" name="contactMessage" placeholder="Please enter your message here..." rows="5"></textarea>
							</div>
						</div>
						<!-- Form actions -->
						<div class="form-group">
							<div class="col-md-12 text-center">
								<button type="submit" class="btn btn-primary btn-lg">Submit</button>
							</div>
						</div>
          			</fieldset>
          		</form>
        	</div>
		  </div>
		  <div class="col-md-6">
			
		</div>
	</div>
</div>
</section>
@stop
@section('modals')
	@include('modals.login')
	@include('modals.register')
	<script type="text/javascript">
		$('#register-modal').on('shown.bs.modal', function (e) {
			$('#login-modal').modal('hide');
		})
	</script>
@stop