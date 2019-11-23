@extends('layouts.admin')
@section('content')
    <div class="row text-center mt-5">
        <h3>{{ isset($brand) ? "Update Brand" : "Add Brand"}}</h3>
    </div>
    <div class="row">
        <div class="col-sm-12 col-md-4 offset-md-4">
            <img class="img-fluid" id="logo" width="96" height="96" src="{{ isset($brand) ?  asset($brand->logo) : asset('images/brands/no-image-found.png') }}">
        </div>
        <div class="col-sm-12 col-md-6 offset-md-3">
        @if(isset($brand))
            <form enctype="multipart/form-data" method="POST" action="{{ route('brands.update', ['brand' => $brand->id]) }}">
                @method('PATCH')
        @else
            <form enctype="multipart/form-data" method="POST" action="{{ route('brands.store') }}">
        @endif
                @csrf
                <div class="form-group">
                    <label for="brandLogo">Brand Logo</label>
                    <input type="file" name="logo" class="form-control-file {{ $errors->has('logo') ? 'is-invalid' : ''}}" id="brandLogo" value="{{ old('logo') ? old('logo') : (isset($brand) ? $brand->logo : '') }}">
                    @if ($errors->has('logo'))
                        <div class="error text-danger"><small>{{ $errors->first('logo') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="brandName">Brand Name</label>
                    <input type="text" value="{{ old('name') ? old('name') : (isset($brand) ? $brand->name : '') }}" name="name" class="form-control {{ $errors->has('name') ? 'is-invalid' : ''}} " id="brandName" placeholder="Enter Brand Name">
                    @if ($errors->has('name'))
                        <div class="error text-danger"><small>{{ $errors->first('name') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <input type="submit" value="{{ isset($brand) ? 'Update' : 'Add' }}" class="form-control btn btn-primary">
                </div>
            </form>
        </div>
    </div>  
@stop
@section('custom-js')
<script type="text/javascript">
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#logo').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#brandLogo").change(function() {
        readURL(this);
    });
</script>
@stop