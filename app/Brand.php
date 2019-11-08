<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Brand extends Model
{
    const IMAGE_FOLDER ='/images/brands/';

    public function getLogoAttribute(string $value): string
    {
        return self::IMAGE_FOLDER . $value;
    }
}
