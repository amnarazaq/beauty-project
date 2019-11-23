<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class CategoriesTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $categories = [
            ['name' => 'Face Primer'],
            ['name' => 'Concealer'],
            ['name' => 'Foundation'],
            ['name' => 'Face Powder'],
            ['name' => 'BB Cream'],
            ['name' => 'Blush'],
            ['name' => 'Highlight'],
            ['name' => 'Contour'],
            ['name' => 'Bronzer'],
            ['name' => 'Setting Spray'],
            ['name' => 'Setting Powder'],
            ['name' => 'Eye Primer'],
            ['name' => 'Mascara'],
            ['name' => 'Eyelash Curler'],
            ['name' => 'Eyelash Glue'],
            ['name' => 'Extension Eyelashes'],
            ['name' => 'Eyebrow Pencil'],
            ['name' => 'Eyebrow Gels'],
            ['name' => 'Eyebrow Wax'],
            ['name' => 'Eyebrow Powder'],
            ['name' => 'Eyeliner'],
            ['name' => 'Eyeshadow'],
            ['name' => 'Lipstick'],
            ['name' => 'Lip Gloss'],
            ['name' => 'Lip Liner'],
            ['name' => 'Lip Balm'],
            ['name' => 'Lip Primer'],
            ['name'=>'kajal']
        ];

        DB::table('categories')->insert($categories);
    }
}
