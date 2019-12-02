@extends('layouts.admin')
@section('content')
<div class="mt-5">
    <table class="table table-striped table-hover table-responsive-sm">
        <thead class="thead-dark">
            <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Created Date</th>
                <th scope="col">Actions</th>
            </tr> 
        </thead>
        <tbody>
            @forelse ($users as $index => $user)
                <tr>
                    <th scope="row" class="align-middle">{{ (($users->currentPage() - 1)  * 10) + ($index + 1) }}</th>
                    <td class="align-middle">{{ $user->name }}</td>
                    <td class="align-middle">{{ $user->email }}</td>
                    <td class="align-middle">{{ $user->created_at }}</td>
                    <td class="align-middle">
                        <a href="javascript:{}" onclick="document.getElementById('my_form').submit();">
                            <i class="fa fa-trash text-danger" aria-hidden="true"></i>
                        </a>
                        <form method="POST" action="{{ route('users.delete', [$user->id])}}" id="my_form">
                            {{ csrf_field() }}
                            {{ method_field('DELETE') }}
                         </form>
                    </td>
                </tr>
            @empty
                <tr>
                    <td colspan="3">No User Found.</td>
                </tr>
            @endforelse
        </tbody>
    </table>
    {{ $users->links() }}
</div>
@stop