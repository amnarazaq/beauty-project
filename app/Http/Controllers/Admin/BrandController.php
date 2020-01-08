<?php

namespace App\Http\Controllers\Admin;

use App\Brand;
use App\Http\Controllers\Controller;
use App\Http\Requests\BrandForm;
use Illuminate\Support\Facades\File;

class BrandController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $brands = Brand::orderBy('name')->paginate(10);
        return view('admin.brand.index', compact('brands'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('admin.brand.createEditForm');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \App\Http\Requests\BrandForm  $request
     * @return \Illuminate\Http\Response
     */
    public function store(BrandForm $request)
    {
        
        $filename = preg_replace("![^a-z]+!i", "-", $request->name);
        $image = $request->file('logo');
        $filename = $filename .  '.' . $image->getClientOriginalExtension();
        $destinationPath = public_path('/images/brands');
        $image->move($destinationPath, $filename);

        $brand = new Brand();
        $brand->name = $request->name;
        $brand->logo = $filename;
        $brand->save();

        return redirect()->route('brands')->with('success',  'New Brand Successfully created.');
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Brand  $brand
     * @return \Illuminate\Http\Response
     */
    public function show(Brand $brand)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Brand  $brand
     * @return \Illuminate\Http\Response
     */
    public function edit(Brand $brand)
    {
        return view('admin.brand.createEditForm', compact('brand'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \App\Http\Requests\BrandForm  $request
     * @param  \App\Brand  $brand
     * @return \Illuminate\Http\Response
     */
    public function update(BrandForm $request, Brand $brand)
    {
        
        if ($request->hasFile('logo')) {
            if ($brand->name !== $request->name) {
                File::delete(public_path($brand->logo));
            }
            $filename = preg_replace("![^a-z]+!i", "-", $request->name);
            $image = $request->file('logo');
            $filename = $filename .  '.' . $image->getClientOriginalExtension();
            $destinationPath = public_path('/images/brands');
            $image->move($destinationPath, $filename);
            $brand->logo = $filename;
        }

        $brand->name = $request->name;
        $brand->save();

        return redirect()->route('brands')->with('success',  'Brand Successfully updated.');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Brand  $brand
     * @return \Illuminate\Http\Response
     */
    public function destroy(Brand $brand)
    {
        $brand->delete();
        return redirect()->route('brands')->with('success',  'Brand Successfully deleted.');
    }
}
