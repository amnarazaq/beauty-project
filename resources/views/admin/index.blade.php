@extends('layouts.admin')
@section('content')
<div class="row mt-5">
  <div class="col-sm-6 col-lg-3">
    <div class="card text-white bg-info">
      <div class="card-body pb-0">
        <div class="text-value">{{ $users }}</div>
        <div>Registered Users</div>
      </div>
      <div class="chart-wrapper mt-3 mx-3" style="height:70px;">
        <canvas class="chart" id="card-chart1" height="70"></canvas>
      </div>
    </div>
  </div>
  <!-- /.col-->
  <div class="col-sm-6 col-lg-3">
    <div class="card text-white bg-primary">
      <div class="card-body pb-0">
        <button class="btn btn-transparent p-0 float-right" type="button">
          <i class="icon-location-pin"></i>
        </button>
        <div class="text-value">{{ $categories }}</div>
        <div>Number of Categories</div>
      </div>
      <div class="chart-wrapper mt-3 mx-3" style="height:70px;">
        <canvas class="chart" id="card-chart2" height="70"></canvas>
      </div>
    </div>
  </div>
  <!-- /.col-->
  <div class="col-sm-6 col-lg-3">
    <div class="card text-white bg-warning">
      <div class="card-body pb-0">
        <div class="text-value">{{ $products }}</div>
        <div>Available Products</div>
      </div>
      <div class="chart-wrapper mt-3" style="height:70px;">
        <canvas class="chart" id="card-chart3" height="70"></canvas>
      </div>
    </div>
  </div>
  <!-- /.col-->
  <div class="col-sm-6 col-lg-3">
    <div class="card text-white bg-danger">
      <div class="card-body pb-0">
        <div class="text-value">{{ $brands }}</div>
        <div>Total Brands</div>
      </div>
      <div class="chart-wrapper mt-3 mx-3" style="height:70px;">
        <canvas class="chart" id="card-chart4" height="70"></canvas>
      </div>
    </div>
  </div>
  <!-- /.col-->
</div>

@stop