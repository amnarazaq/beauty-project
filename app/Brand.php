<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Brand extends Model
{
    /**
     * Indicates if the model should be timestamped.
     *
     * @var bool
     */
    public $timestamps = false;
    
    const IMAGE_FOLDER ='/images/brands/';

    public function getLogoAttribute(string $value): string
    {
        return self::IMAGE_FOLDER . $value;
    }

    public function products()
    {
        return $this->hasMany(Product::class);
    }
}
