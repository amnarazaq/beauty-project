@extends('layouts.admin')
@section('content')
<div class="mt-5">
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
                        <a href="#" class="mr-2" title="edit">
                            <i class="fa fa-pencil fa-2x text-warning" aria-hidden="true"></i>
                        </a>
                        <a href="#" title="delete">
                            <i class="fa fa-trash fa-2x text-danger" aria-hidden="true"></i>
                        </a>
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