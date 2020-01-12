@extends('layouts.admin')
@section('content')
<div class="mt-5">
<div class="text-right">
        <a href="{{ route('categories.create') }}" class="btn btn-primary">+ Add Category</a>
    </div>
    <table class="table table-striped table-hover table-responsive-sm">
        <thead class="thead-dark">
            <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Actions</th>
            </tr> 
        </thead>
        <tbody>
            @forelse ($categories as $index => $category)
                <tr>
                    <th scope="row" class="align-middle">{{ (($categories->currentPage() - 1)  * 10) + ($index + 1) }}</th>
                    <td class="align-middle">{{ $category->name }}</td>
                    <td class="align-middle">
                    <a href="{{ route('categories.edit', [$category->id]) }}" class="mr-2" title="edit">
                            <i class="far fa-edit text-primary" aria-hidden="true"></i>
                        </a>
                        <a href="javascript:{}" onclick="document.getElementById('my_form{{ $category->id }}').submit();">
                            <i class="fa fa-trash text-danger" aria-hidden="true"></i>
                        </a>
                        <form method="POST" action="{{ route('categories.delete', [$category->id])}}" id="my_form{{ $category->id }}">
                            {{ csrf_field() }}
                            {{ method_field('DELETE') }}
                         </form>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="3">No Categories Found.</td>
                </tr>
            @endforelse
        </tbody>
    </table>
    {{ $categories->links() }}
</div>
@stop