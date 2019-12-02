<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class BrandForm extends FormRequest
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
            $logo = 'nullable|max:2048';
        } else {
            $logo = 'required|max:2048';
        }

        return [
            'name' => 'required|max:50|regex:/^[\pL\s\-]+$/u|unique:brands,name,' .$this->brand->id,
            'logo' => $logo,
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
            'name.required' => 'A Brand name is required',
            'name.unique'  => 'Brand name already exists. Use different name.',
            'name.max' => 'Max character limit is 50',
            'logo.required' => 'Brand logo is required',
        ];
    }
}
