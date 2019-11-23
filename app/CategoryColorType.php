<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class CategoryColorType extends Model
{
   /**
     * Indicates if the model should be timestamped.
     *
     * @var bool
     */
    public $timestamps = false;

    public function products()
    {
        return $this->hasMany(Product::class);
    }
}
