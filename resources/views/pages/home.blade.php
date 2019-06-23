@extends('layouts.app')
@section('main-banner')
<header id="banner" class="col-sm-12">
    <div class="d-flex justify-content-center col-sm-8 align-items-center h-100 container">
    	<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active ">
              <div class="title d-flex justify-content-center" style="font-family:  Arial Black"><h1>Welcome</h1></div>
              <div class="description" style="font-family:  Georgia;"><h2>To a Glamorous Beauty website</h2></div>
            </div>
            <div class="carousel-item">
              <div class="description d-flex justify-content-center col-sm-10" style="font-family:  Arial Black;"><h1>A thing of beauty is a joy forever for women</h1></div>
            </div>
          </div>
        </div>
    </div>
</header>
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
@stop
@section('modals')
	@include('modals.login')
	@include('modals.register')
@stop