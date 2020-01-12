@extends('layouts.admin')
@section('content')
<div class="mt-5">
<div class="text-right">
        <a href="{{ route('colortypes.create') }}" class="btn btn-primary">+ Add Category Color Type</a>
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
            @forelse ($categoryColorTypes as $index => $colortype)
                <tr>
                    <th scope="row" class="align-middle">{{ (($categoryColorTypes->currentPage() - 1)  * 10) + ($index + 1) }}</th>
                    <td class="align-middle">{{ $colortype->name }}</td>
                    <td class="align-middle">
                        <a href="{{ route('colortypes.edit', [$colortype->id]) }}" class="mr-2" title="edit">
                            <i class="far fa-edit text-primary" aria-hidden="true"></i>
                        </a>
                        <a href="javascript:{}" onclick="document.getElementById('my_form{{ $colortype->id }}').submit();">
                            <i class="fa fa-trash text-danger" aria-hidden="true"></i>
                        </a>
                        <form method="POST" action="{{ route('colortypes.delete', [$colortype->id])}}" id="my_form{{ $colortype->id }}">
                            {{ csrf_field() }}
                            {{ method_field('DELETE') }}
                        </form>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="3">No Categories Color Type Found.</td>
                </tr>
            @endforelse
        </tbody>
    </table>
    {{ $categoryColorTypes->links() }}
</div>
@stop