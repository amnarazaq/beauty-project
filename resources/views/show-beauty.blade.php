@extends('layouts.app')
@section('content')
<section id="new-header">
    @if (session('status'))
        <div class="alert alert-success" role="alert">
            {{ session('status') }}
        </div>
    @endif
    <div class="container" style="margin-top:75px">
        <div class="row d-flex justify-content-center">
            <div class="font-weight-bold pl-2 pr-2" style=" font-family: HelveticaNeueW01-77BdCn_692722,arial,sans-serif;
                font-size: 24px">Here Yours
            </div>
            <div class="banner-image-large">
                <img alt="Get the look"src="{{ asset('/images/look.png') }}">
            </div>
        </div>
    </div>
</section>
<section id="output-image">
    <div class="container mt-4">
        <div class="row d-flex justify-content-center">
            <div class="col-md-6 d-flex justify-content-center">
                <div class="row">
                    <div class="col-md-12" id="before-makeup">
                        <img width="270px" height="300px" src="{{ asset('storage/users/' . $user->id . '/original.jpg') }}">
                    </div>
                </div>
            </div>
            <div class="col-md-6 d-flex justify-content-center">
                <div class="row">
                    <div class="col-md-12" id="before-makeup">
                        <img width="270px" height="300px" src="{{ asset('storage/users/' . $user->id . '/result.jpg') }}">
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<section id="tutorial">
    <div class="container mt-5">
        <div class="row d-flex justify-content-left">
            <div class="font-weight-bold pl-2 pr-2" style=" font-family:arial,sans-serif;font-size: 28px">
                How to do makeup step by step
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Start by perfecting your skin
                </div>
                <p class="pl-4 pr-5">So that makeup blends in easily‚ first wash with cleanser and a cloth to gently exfoliate your face.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/1.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Mosturize you skin
                </div>
                <p class="pl-4 pr-5">With any kind of lotion or primer so that foundation can easily set on your face.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/2.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Conceal if any flaws
                </div>
                <p class="pl-4 pr-5">For visible breakouts,any dark spots or deep undereye circles, use a pigment-rich concealer for even tone your skin.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/3.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Apply Foundation
                </div>
                <p class="pl-4 pr-5">Which match with your skin color.We prefer this foundation that our expert AI team found by matching it with your skin color.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/4.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Use bake powder if you needed
                </div>
                <p class="pl-4 pr-5">If your skin gets shiny, follow with an oil-absorbing powder.Or if your skin is very oily, skip the tinted moisturizer and use only concealer and powder.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/5.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Apply blush or contour
                </div>
                <p class="pl-4 pr-5">If you need to contour your face you can do it. Apply this warm cheek color to add glow on your skin.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/6.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Do your eyes
                </div>
                <p class="pl-4 pr-5">as our AI team select and done on your eyes according to your dress color and event for which you want to do makeup.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/7.png') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    shape your eyebrows
                </div>
                <p class="pl-4 pr-5">by using brown pencil.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/8.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Apply eyeliner
                </div>
                <p class="pl-4 pr-5">As we select according to your eyes shape.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/9.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Enhance your lash
                </div>
                <p class="pl-4 pr-5">Applying mascara or lash extension.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/10.jpg') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    do your lips
                </div>
                <p class="pl-4 pr-5">Use this lip color which perfectly suits you..</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/11.png') }}">
            </div>
        </div>
        <div class="row d-flex justify-content-left mt-3">
            <div class="col-sm-7">
                <div class="pl-2" style=" font-family:arial,sans-serif;font-size: 20px">
                    Highlight your features
                </div>
                <p class="pl-4 pr-5">such that your cheek bone, upper lip point and lower lip point or under your eyebrow.</p>
            </div>
            <div class="col-sm-5">
                <img class="product img-fluid pl-4 pr-5" style="background-color: white" width="150px" height="150px" src="{{ asset('/images/toturial-image/12.jpg') }}">
            </div>
        </div>
    </div>
</section>
@stop