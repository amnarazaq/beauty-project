<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class ProductForm extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return Auth::user()->hasRole('admin');
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        if (Request::isMethod('patch')) {
            $image = 'nullable|max:2048';
            $name = ',name,' . $this->get('id');
        } else {
            $image = 'required|max:2048';
            $name = '';
        }

        return [
            'name' => 'required|max:50|regex:/^[\pL\s\-]+$/u|unique:products' . $name,
            'image' => $image,
        ];
    }

    /**
     * Get the error messages for the defined validation rules.
     *
     * @return array
     */
    public function messages()
    {
        return [
            'name.required' => 'A Product name is required',
            'name.unique'  => 'Product name already exists. Use different name.',
            'name.max' => 'Max character limit is 50',
            'image.required' => 'Product image is required',
        ];
    }
}
