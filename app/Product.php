<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    //Image path will be products/{categoryId}/{brandId}/{imageName}
    public function category()
    {
        return $this->belongsTo(Category::class);
    }

    public function brand()
    {
        return $this->belongsTo(Brand::class);
    }
}
