@extends('layouts.admin')
@section('content')
<div class="mt-5">
    <div class="text-right">
        <a href="{{ route('brands.create') }}" class="btn btn-primary">+ Add Brand</a>
    </div>
    <table class="table table-striped table-hover table-responsive-sm">
        <thead class="thead-dark">
            <tr>
                <th scope="col">#</th>
                <th scope="col">Logo</th>
                <th scope="col">Name</th>
                <th scope="col">Actions</th>
            </tr> 
        </thead>
        <tbody>
            @forelse ($brands as $index => $brand)
                <tr>
                    <th scope="row" class="align-middle">{{ (($brands->currentPage() - 1)  * 10) + ($index + 1) }}</th>
                    <td><img class="img-fluid" src="{{ asset($brand->logo) }}" width="64" height="64"/></td>
                    <td class="align-middle">{{ $brand->name }}</td>
                    <td class="align-middle">
                        <a href="{{ route('brands.edit', [$brand->id]) }}" class="mr-2" title="edit">
                            <i class="fa fa-pencil fa-2x text-warning" aria-hidden="true"></i>
                        </a>
                        <a href="{{ route('brands.delete', [$brand->id]) }}" title="delete">
                            <i class="fa fa-trash fa-2x text-danger" aria-hidden="true"></i>
                        </a>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="4">No Brands Found.</td>
                </tr>
            @endforelse
        </tbody>
    </table>
    {{ $brands->links() }}
</div>
@stop