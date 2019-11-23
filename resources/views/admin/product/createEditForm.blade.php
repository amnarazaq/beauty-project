@extends('layouts.admin')
@section('content')
    <div class="row text-center mt-5">
        <h3>{{ isset($product) ? "Update Product" : "Add Product"}}</h3>
    </div>
    <div class="row">
        <div class="col-sm-12 col-md-6 offset-md-3">
        @if(isset($product))
            <form enctype="multipart/form-data" method="POST" action="{{ route('products.update', ['products' => $product->id]) }}">
                @method('PATCH')
        @else
            <form enctype="multipart/form-data" method="POST" action="{{ route('products.store') }}">
        @endif
                @csrf
                <div class="form-group">
                    <label for="category">Category</label>
                    <select class="custom-select" id="category" name="category">
                         @foreach($categories as $category)
                            <option value="{{ $category->id }}" {{ isset($product) && $product->category_id == $category->id ? 'selected' :  '' }}>{{ $category->name }}</option>
                        @endforeach
                    </select>
                    @if ($errors->has('category'))
                        <div class="error text-danger"><small>{{ $errors->first('category') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="brand">Brand</label>
                    <select class="custom-select" id="brand" name="brand">
                        @foreach($brands as $brand)
                            <option value="{{ $brand->id }}" {{ isset($product) && $product->brand_id == $brand->id ? 'selected' :  '' }}>{{ $brand->name }}</option>
                        @endforeach
                    </select>
                    @if ($errors->has('brand'))
                        <div class="error text-danger"><small>{{ $errors->first('brand') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="color_type">Color Type</label>
                    <select class="custom-select" id="color_type" name="color_type">
                        @foreach($colorTypes as $colorType)
                            <option value="{{ $colorType->id }}" {{ isset($product) && $product->category_color_type_id == $colorType->id ? 'selected' :  '' }}>{{ $colorType->name }}</option>
                        @endforeach
                    </select>
                    @if ($errors->has('color_type'))
                        <div class="error text-danger"><small>{{ $errors->first('color_type') }}</small></div>
                    @endif
                </div>
                
                <div class="form-group">
                    <label for="productName">Product Name</label>
                    <input type="text" value="{{ old('name') ? old('name') : (isset($product) ? $product->name : '') }}" name="name" class="form-control {{ $errors->has('name') ? 'is-invalid' : ''}} " id="ProductName" placeholder="Enter Product Name">
                    @if ($errors->has('name'))
                        <div class="error text-danger"><small>{{ $errors->first('name') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <div class="col-sm-12 col-md-4 offset-md-4">
                        <img class="img-fluid" id="image" width="96" height="96" src="{{ isset($product) ?  asset($product->image) : asset('images/brands/no-image-found.png') }}">
                    </div>
                    <label for="productImage">Product Image</label>
                    <input type="file" name="image" class="form-control-file {{ $errors->has('image') ? 'is-invalid' : ''}}" id="productImage" value="{{ old('image') ? old('image') : (isset($product) ? $product->image : '') }}">
                    @if ($errors->has('image'))
                        <div class="error text-danger"><small>{{ $errors->first('image') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="productColorName">Product Color Name</label>
                    <input type="text" value="{{ old('color_name') ? old('color_name') : (isset($product) ? $product->color_name : '') }}" name="colorName" class="form-control {{ $errors->has('color_name') ? 'is-invalid' : ''}} " id="ProductColorName" placeholder="Enter Product Color Name">
                    @if ($errors->has('color_name'))
                        <div class="error text-danger"><small>{{ $errors->first('color_name') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="productColorCodeHex">Product Color Code</label>
                    <input type="text" minlength="6" maxlength="6" value="{{ old('color_code_hex') ? old('color_code_hex') : (isset($product) ? $product->color_code_hex : '') }}" name="colorCodeHex" class="form-control {{ $errors->has('color_code_hex') ? 'is-invalid' : ''}} " id="ProductColorCodeHex" placeholder="Enter Product color code in hex">
                    @if ($errors->has('color_code_hex'))
                        <div class="error text-danger"><small>{{ $errors->first('color_code_hex') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <input type="submit" value="{{ isset($product) ? 'Update' : 'Add' }}" class="form-control btn btn-primary">
                </div>
            </form>
        </div>
    </div>  
@stop
@section('custom-js')
<script type="text/javascript">
    $(document).ready(function($) {
      // Example using an event, to change the color of the .jumbotron background:
      $('#ProductColorCodeHex').on('input', function(event) {
          if (event.target.value.length < 3) {
            $('#ProductColorCodeHex').css('background-color', '#fff');
          } else {
            $('#ProductColorCodeHex').css('background-color', '#' + event.target.value);
          }
      });
    });
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#image').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#productImage").change(function() {
        readURL(this);
    });
</script>
@stop