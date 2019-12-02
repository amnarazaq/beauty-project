@extends('layouts.app')
@section('main-banner')
<section id="banner" class="col-sm-12">
    <div class="d-flex justify-content-center col-sm-8 align-items-center h-100 container">
    	<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active ">
            	<div class="title d-flex justify-content-center  col-sm-10" style="font-family:  Arial Black"><h1>Welcome</h1></div>
				<div class="description" style="font-family:  Georgia;">
				  <h2>To a Glamorous Beauty website</h2>
					@auth 
						<a href="{{ route('home') }}" class="btn btn-cam">Try Virtual Look</a>
					@endauth
					@guest
					<button type="button" class="btn btn-cam" data-toggle="modal" data-target="#login-modal">
						Try Virtual Look
					</button>
					@endguest
				</div>
            </div>
            <div class="carousel-item">
              <div class="description d-flex justify-content-center col-sm-10" style="font-family:  Arial Black;"><h1>A thing of beauty is a joy forever for women</h1></div>
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
	</div>
</section>
<section id="contact-us">
<div class="container py-5">
	<div class="row">
		<div class="col-md-6">
			
		</div>
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