@extends('layouts.admin')
@section('content')
<div class="mt-5">
<div class="text-right">
        <a href="{{ route('products.create') }}" class="btn btn-primary">+ Add Product</a>
    </div>
    <table class="table table-striped table-hover table-responsive-sm">
        <thead class="thead-dark">
            <tr>
                <th scope="col">#</th>
                <th scope="col">Image</th>
                <th scope="col">Category</th>
                <th scope="col">Brand</th>
                <th scope="col">Name</th>
                <th scope="col">Color</th>
                <th scope="col">Actions</th>
            </tr> 
        </thead>
        <tbody>
            @forelse ($products as $index => $product)
                <tr>
                    <th scope="row" class="align-middle">{{ (($products->currentPage() - 1)  * 10) + ($index + 1) }}</th>
                    <td class="align-middle">
                        <img class="img-fluid" width="64px" height="64px" style="background-color:white" src="{{ asset('/images/products/'.$product->category->id.'/'.$product->brand->id.'/'.$product->image) }}">
                    </td>
                    <td class="align-middle">{{ $product->category->name }}</td>
                    <td class="align-middle">{{ $product->brand->name }}</td>
                    <td class="align-middle">{{ $product->name }}</td>
                    <td class="align-middle">
                        <div width="32px" height="32px" style="background-color:#{{ $product->color_code_hex }};">&nbsp;</div>
                        {{ $product->color_name }}
                    </td>
                    <td class="align-middle">
                    <a href="{{ route('products.edit', [$product->id]) }}" class="mr-2" title="edit">
                            <i class="far fa-edit text-primary" aria-hidden="true"></i>
                        </a>
                        <a href="{{ route('products.delete', [$product->id]) }}" title="delete">
                            <i class="fa fa-trash text-danger" aria-hidden="true"></i>
                        </a>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="7">No products Found.</td>
                </tr>
            @endforelse
        </tbody>
    </table>
    {{ $products->links() }}
</div>
@stop