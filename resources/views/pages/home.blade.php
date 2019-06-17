@extends('layouts.app')
@section('main-banner')
<div id="banner">
        <div class="d-flex justify-content-center align-items-center h-100">
        	<div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <div class="title"><h3>Title</h3></div>
                  <div class="description">My First Title</div>
                </div>
                <div class="carousel-item">
                  <div class="title"><h3>Second Title</h3></div>
                  <div class="description">My Second Title</div>
                </div>
                <div class="carousel-item">
                  <div class="title"><h3>Third Title</h3></div>
                  <div class="description">My Third Title</div>
                </div>
              </div>
            </div>
        </div>
    </div>
@stop
@section('content')
<section id="about-us">
	<div class="container py-5">
		<div class="row">
			<div class="col-sm-12 text-center"><strong><h2>About Us</h2></strong></div>
		</div>
		<div class="row">
			<div class="col-sm-12 offset-lg-5 col-lg-7 mt-3">
				Whether you want a new look for a special occasion or you want to do regular makeup this website will help you in choosing a look which suits you perfect in few minutes. This website is for ease of customers to decide which look will suits on them and which product is suitable for their skin in less time.
			</div>
		</div>
	</div>
</section>
<section id="how-it-works">
	<div class="container py-5">
		<div class="row">
			<div class="col-sm-12 text-center"><strong><h2>How it Works</h2></strong></div>
		</div>
	</div>
</section>
@stop
@section('modals')
	@include('modals.login')
@stop