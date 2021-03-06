<?php

namespace App\Http\Controllers;

use Faker\Provider\Image;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Storage;

class BeautyController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return view('show-beauty');
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $lookChoice = $request->get('lookChoice');
        $dressColor = $request->get('dressColor');

        $user = Auth::user();
        $fileName = 'users/' . $user->id . '/original.jpg';
        if ($request->has('cameraImage')) {
            $photo =$request->get('cameraImage');
            if(strlen($photo) > 128) {
                list($ext, $data)   = explode(';', $photo);
                list(, $data)       = explode(',', $data);
                $data = base64_decode($data);
                Storage::disk('public')->put($fileName, $data);
            }
        } else {
            $image = $request->file('picture');
            Storage::disk('public')->put($fileName, $image->get());
        }

        //execute python scripts
        $cmd = sprintf('python %s %s %s %s %s',
            storage_path('app/scripts/inputfile.py'), 
            storage_path('app/public/' . $fileName),
            $lookChoice,
            $dressColor,
            storage_path('app/testImages')
        );
        ob_start();
        $output = [];
        exec($cmd . " 2>&1", $output);
        Log::info(print_r($output, true));
        $result = ob_get_contents();
        ob_end_clean();

        return view('show-beauty', compact('user'));
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
