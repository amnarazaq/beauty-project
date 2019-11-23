<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class BrandsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $brands = [
            [
                'name' => 'Estee Lauder',
                'logo' => 'estee-lauder.png'
            ],
            [
                'name' => 'Loreal',
                'logo' => 'loreal.png'
            ],
            [
                'name' => 'Maybelline',
                'logo' => 'maybelline.png'
            ],
            [
                'name' => 'Guerlain',
                'logo' => 'guerlain.png'
            ],
            [
                'name' => 'NARS',
                'logo' => 'nars.jpg'
            ],
            [
                'name' => 'Laura Mercier',
                'logo' => 'laura-mercier.png'
            ],
            [
                'name' => 'Chanel',
                'logo' => 'chanel.png'
            ],
            [
                'name' => 'Clarins',
                'logo' => 'clarins.png'
            ],
            [
                'name' => 'Dior',
                'logo' => 'dior.png'
            ],
            [
                'name' => 'Urban Decay',
                'logo' => 'urban-decay.jpg'
            ],
            [
                'name' => 'Sephora',
                'logo' => 'sephora.png'
            ],
            [
                'name' => 'Yves Saint Laurent',
                'logo' => 'yves-saint-laurent.png'
            ],
            [
                'name' => 'MAC',
                'logo' => 'mac.png'
            ],
            [
                'name' => 'Covergirl',
                'logo' => 'covergirl.jpg'
            ],
            [
                'name' => 'Clinique',
                'logo' => 'clinique.png'
            ],
            [
                'name' => 'ELF',
                'logo' => 'elf.png'
            ],
            [
                'name' => 'NYX',
                'logo' => 'nyx.png'
            ],
            [
                'name' => 'Revlon',
                'logo' => 'revlon.png'
            ],
            [
                'name' => 'Elizabeth Arden',
                'logo' => 'elizabeth-arden.png'
            ],
            [
                'name' => 'Burberry',
                'logo' => 'burberry.png'
            ],
            [
                'name' => 'Napoleon Perdis',
                'logo' => 'napoleon-perdis.png'
            ],
            [
                'name' => 'Mecca',
                'logo' => 'mecca.png'
            ],
            [
                'name' => 'Too Faced',
                'logo' => 'too-faced.jpg'
            ],
            [
                'name' => 'Benefit',
                'logo' => 'benefit.jpg'
            ],
            [
                'name' => 'Anastasia',
                'logo' => 'anastasia.jpg'
            ],
            [
                'name' => 'Smashbox',
                'logo' => 'smashbox.jpg'
            ],
            [
                'name' => 'IT Cosmetics',
                'logo' => 'it-cosmetics.png'
            ],
            [
                'name' => 'The Balm',
                'logo' => 'the-balm.jpg'
            ],
            [
                'name' => 'Tom Ford',
                'logo' => 'tom-ford.png'
            ],
            [
                'name' => 'Kylie',
                'logo' => 'kylie.jpg'
            ],
            [
                'name' => 'Neutrogena',
                'logo' => 'Neutrogena.png'
            ],
            [
                'name' => 'Etude',
                'logo' => 'Etude.png'
            ],
            [
                'name' => 'Avon',
                'logo' => 'avon.png'
            ],
            [
                'name' => 'Huda Beauty',
                'logo' => 'huda-beauty.png'
            ],
            [
                'name' => 'BareMinerals',
                'logo' => 'bareminerals.png'
            ]
        ];

        DB::table('brands')->insert($brands);
    }
}
