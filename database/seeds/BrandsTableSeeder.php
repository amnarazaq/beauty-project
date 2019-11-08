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
                'logo' => 'nars.png'
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
                'logo' => 'urban-decay.png'
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
                'logo' => 'covergirl.png'
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
                'logo' => 'too-faced.png'
            ],
            [
                'name' => 'Benefit',
                'logo' => 'benefit.png'
            ],
            [
                'name' => 'Anastasia',
                'logo' => 'anastasia.png'
            ],
            [
                'name' => 'Smashbox',
                'logo' => 'smashbox.png'
            ],
            [
                'name' => 'IT Cosmetics',
                'logo' => 'it-cosmetics.png'
            ],
            [
                'name' => 'The Balm',
                'logo' => 'the-balm.png'
            ],
            [
                'name' => 'Tom Ford',
                'logo' => 'tom-ford.png'
            ],
            [
                'name' => 'Kylie',
                'logo' => 'kylie.png'
            ],
            [
                'name' => 'Neutrogena',
                'logo' => 'neutrogena.png'
            ],
            [
                'name' => 'Etude',
                'logo' => 'etude.png'
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
