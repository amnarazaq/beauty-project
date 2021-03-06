<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    //Image path will be products/{categoryId}/{brandId}/{imageName}
    /**
     * Indicates if the model should be timestamped.
     *
     * @var bool
     */
    public $timestamps = false;
    
    const IMAGE_FOLDER ='/images/products';
    public function category()
    {
        return $this->belongsTo(Category::class);
    }

    public function brand()
    {
        return $this->belongsTo(Brand::class);
    }
    
    public function color_type()
    {
        return $this->belongsTo(CategoryColorType::class, 'category_color_type_id');
    }

    public function getImageAttribute(string $value): string
    {
        return self::IMAGE_FOLDER . '/' . $this->category->id . '/' . $this->brand->id . '/' . $value;
    }
}
