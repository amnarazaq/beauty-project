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
    
    const IMAGE_FOLDER ='/images/products/{{ category_id }}/{{ brand_id }}';
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
        return $this->belongsTo(CategoryColorType::class);
    }
}
