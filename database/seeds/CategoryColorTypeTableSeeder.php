<?php

use Illuminate\Database\Seeder;

class CategoryColorTypeTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $colorTypes = [
            [
                'name' => 'White Tan'
            ],
            [
                'name' => 'Extremely Fair'
            ],
            [
                'name' => 'Fair Redspot'
            ],
            [
                'name' => 'Natural Redspot'
            ],
            [
                'name' => 'Natural'
            ],
            [
                'name' => 'Black Brown'
            ],
            [
                'name' => 'Brown'
            ],
            [
                'name' => 'Dark Brown'
            ],
            [
                'name' => 'Fair'
            ],
            [
                'name' => 'Natural White'
            ],
            [
                'name' => 'Natural Brown'
            ],
            [
                'name' => 'Dark'
            ],
            [
                'name' => 'Tan'
            ],
            [
                'name' => 'Skin Pale'
            ],
            [
                'name' => 'Pink'
            ],
            [
                'name' => 'Peach'
            ],
            [
                'name' => 'Dark Red'
            ],
            [
                'name' => 'Bright Pink'
            ],
            [
                'name' => 'Dark Pink'
            ],
            [
                'name' => 'Orange'
            ],
            [
                'name' => 'Maroon'
            ],
            [
                'name' => 'Purple'
            ],
            [
                'name' => 'Black'
            ],
            [
                'name' => 'Off White'
            ],
            [
                'name' => 'Brown'
            ],
            [
                'name' => 'Casual'
            ],
            [
                'name' => 'Party'
            ],
            [
                'name' => 'Bridal'
            ],
            
        ];

        DB::table('category_color_type')->insert($colorTypes);
    }
}
