<?php

namespace App\Http\Controllers\Admin;

use App\Category;
use App\CategoryColorType;
use App\Http\Controllers\Controller;
use App\Http\Requests\CategoryColorTypeForm;

class CategoryColorTypeController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $categoryColorTypes = CategoryColorType::paginate(10);
        return view('admin.category_color_type.index', compact('categoryColorTypes'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('admin.category_color_type.createEditForm');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \App\Http\Requests\CategoryColorTypeForm  $request
     * @return \Illuminate\Http\Response
     */
    public function store(CategoryColorTypeForm $request)
    {
        $colortype = new CategoryColorType();
        $colortype->name = $request->name;
        $colortype->save();

        return redirect()->route('colortypes')->with('success',  'New Category color type Successfully Created.');
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\CategoryColorType  $categorycolortype
     * @return \Illuminate\Http\Response
     */
    public function show(CategoryColorType $categorycolortype)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\CategoryColorType  $categorycolortype
     * @return \Illuminate\Http\Response
     */
    public function edit(CategoryColorType $categorycolortype)
    {
        return view('admin.category_color_type.createEditForm', compact('categorycolortype'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \App\Http\Requests\CategoryColorTypeForm  $request
     * @param  \App\CategoryColorType  $categorycolortype
     * @return \Illuminate\Http\Response
     */
    public function update(CategoryColorTypeForm $request, CategoryColorType $categorycolortype)
    {
        $categorycolortype->name = $request->name;
        $categorycolortype->save();

        return redirect()->route('colortypes')->with('success',  'Category color type Successfully updated.');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\CategoryColorType  $colortycategorycolortypepe
     * @return \Illuminate\Http\Response
     */
    public function destroy(CategoryColorType $categorycolortype)
    {
        $categorycolortype->delete();
        return redirect()->back();
    }
}
