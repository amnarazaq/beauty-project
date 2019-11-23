@extends('layouts.admin')
@section('content')
    <div class="row text-center mt-5">
        <h3>{{ isset($categorycolortype) ? "Update Category Color Type" : "Add Category Color Type" }}</h3>
    </div>
    <div class="row">
        <div class="col-sm-12 col-md-6 offset-md-3">
        @if(isset($categorycolortype))
            <form enctype="multipart/form-data" method="POST" action="{{ route('colortypes.update', ['categorycolortype' => $categorycolortype->id]) }}">
                @method('PATCH')
        @else
            <form enctype="multipart/form-data" method="POST" action="{{ route('colortypes.store') }}">
        @endif
                @csrf
                <div class="form-group">
                    <label for="categorycolortypeName">Category Color Type Name</label>
                    <input type="text" value="{{ old('name') ? old('name') : (isset($categorycolortype) ? $categorycolortype->name : '') }}" name="name" class="form-control {{ $errors->has('name') ? 'is-invalid' : ''}} " id="categorycolortypeName" placeholder="Enter Category color type Name">
                    @if ($errors->has('name'))
                        <div class="error text-danger"><small>{{ $errors->first('name') }}</small></div>
                    @endif
                </div>
                <div class="form-group">
                    <input type="submit" value="{{ isset($categorycolortype )? 'Update' : 'Add' }}" class="form-control btn btn-primary">
                </div>
            </form>
        </div>
    </div>  
@stop