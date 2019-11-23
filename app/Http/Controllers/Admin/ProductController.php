<?php

namespace App\Http\Controllers\Admin;

use App\Brand;
use App\Category;
use App\CategoryColorType;
use App\Http\Controllers\Controller;
use App\Product;
use App\Http\Requests\ProductForm;
use Illuminate\Support\Facades\File;

class ProductController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $products = Product::orderBy('name')->paginate(10);
        return view('admin.product.index', compact('products'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $categories = Category::orderBy('name')->get();
        $brands = Brand::orderBy('name')->get();
        $colorTypes = CategoryColorType::orderBy('name')->get();

        return view('admin.product.createEditForm', compact('categories', 'brands', 'colorTypes'));
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(ProductForm $request)
    {
        $filename = preg_replace("![^a-z]+!i", "-", $request->name);
        $image = $request->file('image');
        $filename = $filename .  '.' . $image->getClientOriginalExtension();
        $destinationPath = public_path('/images/products/{{ category_id }}/{{ brand_id }}');
        $image->move($destinationPath, $filename);

        $product = new Product();
        $product->name = $request->name;
        $product->brand = $request->brand;
        $product->category = $request->category;
        $product->color_type = $request->color_type;
        $product->image = $filename;
        $product->color_name = $request->color_name;
        $product->color_code_hex = $request->colorCodeHex;

        $product->save();

        return redirect()->route('products')->with('success',  'New Product Successfully created.');
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function show(Product $product)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function edit(Product $product)
    {
        $categories = Category::orderBy('name')->get();
        $brands = Brand::orderBy('name')->get();
        $colorTypes = CategoryColorType::orderBy('name')->get();

        return view('admin.product.createEditForm', compact('categories', 'brands', 'colorTypes','product'));
       // return view('admin.product.createEditForm', compact('product'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\ProductForm  $request
     * @param  \App\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function update(ProductForm $request, Product $product)
    {
        if ($request->hasFile('image')) {
            if ($product->name !== $request->name) {
                File::delete(public_path($product->image));
            }
            $filename = preg_replace("![^a-z]+!i", "-", $request->name);
            $image = $request->file('image');
            $filename = $filename .  '.' . $image->getClientOriginalExtension();
            $destinationPath = public_path('/images/brands/{{ category_id }}/{{ brand_id }}');
            $image->move($destinationPath, $filename);
            $product->image = $filename;
        }

        $product->name = $request->name;
        $product->brand = $request->brand;
        $product->category = $request->category;
        $product->color_type = $request->color_type;
        $product->color_name = $request->color_name;
        $product->color_code_hex = $request->colorCodeHex;
        $product->save();

        return redirect()->route('products')->with('success',  'Product Successfully updated.');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function destroy(Product $product)
    {
        $product->delete();
        return redirect()->back;
    }
}
