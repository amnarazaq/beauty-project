@extends('layouts.admin')
@section('content')
    <div class="row text-center mt-5">
        <h3>{{ isset($product) ? "Update Product" : "Add Product"}}</h3>
    </div>
    <div class="row">
        <div class="col-sm-12 col-md-6 offset-md-3">
        @if(isset($product))
            <form enctype="multipart/form-data" method="POST" action="{{ route('categories.update', ['categories' => $product->id]) }}">
                @method('PATCH')
        @else
            <form enctype="multipart/form-data" method="POST" action="{{ route('categories.store') }}">
        @endif
                @csrf
                <div class="form-group">
                    <label for="category">Category</label>
                    <select class="custom-select" id="category" name="category">
                        <option>Select Category</option>
                        @foreach($categories as $category)
                            <option value="{{ $category->name }}">{{ $category->name }}</option>
                        @endforeach
                    </select>
                    @if ($errors->has('category'))
                        <div class="error text-danger"><small>{{ $errors->first('category') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="brand">Brand</label>
                    <select class="custom-select" id="brand" name="brand">
                        <option>Select Brand</option>
                        @foreach($brands as $brand)
                            <option value="{{ $brand->name }}">{{ $brand->name }}</option>
                        @endforeach
                    </select>
                    @if ($errors->has('brand'))
                        <div class="error text-danger"><small>{{ $errors->first('brand') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <label for="color_type">Color Type</label>
                    <select class="custom-select" id="color_type" name="color_type">
                        <option>Select Color Type</option>
                        @foreach($colorTypes as $colorType)
                            <option value="{{ $colorType->name }}">{{ $colorType->name }}</option>
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
                    <input type="submit" value="{{ isset($product) ? 'Update' : 'Add' }}" class="form-control btn btn-primary">
                </div>
            </form>
        </div>
    </div>  
@stop