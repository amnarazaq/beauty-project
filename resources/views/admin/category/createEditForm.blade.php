@extends('layouts.admin')
@section('content')
    <div class="row text-center mt-5">
        <h3>{{ isset($category) ? "Update Category" : "Add Category"}}</h3>
    </div>
    <div class="row">
        <div class="col-sm-12 col-md-6 offset-md-3">
        @if(isset($category))
            <form enctype="multipart/form-data" method="POST" action="{{ route('categories.update', ['categories' => $category->id]) }}">
                @method('PATCH')
        @else
            <form enctype="multipart/form-data" method="POST" action="{{ route('categories.store') }}">
        @endif
                @csrf
                <div class="form-group">
                    <label for="categoryName">Category Name</label>
                    <input type="text" value="{{ old('name') ? old('name') : (isset($category) ? $category->name : '') }}" name="name" class="form-control {{ $errors->has('name') ? 'is-invalid' : ''}} " id="CategoryName" placeholder="Enter Category Name">
                    @if ($errors->has('name'))
                        <div class="error text-danger"><small>{{ $errors->first('name') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <input type="submit" value="{{ isset($category) ? 'Update' : 'Add' }}" class="form-control btn btn-primary">
                </div>
            </form>
        </div>
    </div>  
@stop