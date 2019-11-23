<?php

use Illuminate\Database\Seeder;

class ProductsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $products = [
            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'EFD6B6',
                'color_name' => 'Milkshake 100B',
                'image' => 'milkshake-100b.jpg',
                'category_color_type_id' => '1',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
                
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'F8ECE1',
                'color_name' => 'Angel Food 110N',
                'image' => 'angel-food-110n.jpg',
                'category_color_type_id' => '2',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'F0CDA9',
                'color_name' => 'Vanilla 120B',
                'image' => 'vanilla-120b.jpg',
                'category_color_type_id' => '3',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'EFD6B6',
                'color_name' => 'Panna Cotta 130G',
                'image' => 'panna-cotta-130g.jpg',
                'category_color_type_id' => '4',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'EEC494',
                'color_name' => 'Cashew 140G',
                'image' => 'cashew-140g.png',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'E8C090',
                'color_name' => 'Crème Brulée 150G',
                'image' => 'creme-brulee-150g.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'E8C09A',
                'color_name' => 'Shortbread 200B',
                'image' => 'shortbread-200b.jpg',
                'category_color_type_id' => '4',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'E7BE8E',
                'color_name' => 'Chai 210B',
                'image' => 'chai-210b.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'E5B786',
                'color_name' => 'Custard 220N',
                'image' => 'custard-220n.png',
                'category_color_type_id' => '3',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'E3B991',
                'color_name' => 'Macaroon 230N',
                'image' => 'macaroon-230n.png',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'E4B989',
                'color_name' => 'Toasted Coconut 240N',
                'image' => 'toasted-coconut-240n.png',
                'category_color_type_id' => '5',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'DEAF82',
                'color_name' => 'Cheesecake 250G',
                'image' => 'cheesecake-250g.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'DCB082',
                'color_name' => 'Latte 300N',
                'image' => 'latte-300n.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'D9AB73',
                'color_name' => 'Amaretti 310G',
                'image' => 'amaretti-310g.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'D6A871',
                'color_name' => 'Tres Leches 320G',
                'image' => 'tres-leches-320g.png',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'D29F6A',
                'color_name' => 'Butter Pecan 330N',
                'image' => 'butter-pecan-330n.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'C99658',
                'color_name' => 'Baklava 340G',
                'image' => 'baklava-340g.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],


            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'C38D54',
                'color_name' => 'Dulce De Leche 350G',
                'image' => 'dulce-de-leche-350g.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'BF8B4F',
                'color_name' => 'Macchiato 400G',
                'image' => 'macchiato-400g.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'B58346',
                'color_name' => 'Brown Sugar 410G',
                'image' => 'brown-sugar-410g.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => 'B98449',
                'color_name' => 'Toffee 420G',
                'image' => 'toffee-420g.jpg',
                'category_color_type_id' => '12',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Fauxfilter Foundation',
                'category_id' => '3',
                'brand_id' => '34',
                'color_code_hex' => '83552F',
                'color_name' => 'Nutmeg 520G',
                'image' => 'nutmeg-520g.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'FAC7AA',
                'color_name' => '201 CLASSIC IVORY',
                'image' => '201-classic-ivory.jpg',
                'category_color_type_id' => '3',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'EDB683',
                'color_name' => '202 CREAMY NATURAL',
                'image' => '202-creamy-natural.jpg',
                'category_color_type_id' => '5',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'E5B289',
                'color_name' => '203 NUDE BEIGE',
                'image' => '203-nude-beige.jpg',
                'category_color_type_id' => '5',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'E1AD86',
                'color_name' => '204 Natural BUFF',
                'image' => '204-natural-buff.jpg',
                'category_color_type_id' => '7',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'FAC7AA',
                'color_name' => '205 Natural BEIGE',
                'image' => '205-natural-beige.jpg',
                'category_color_type_id' => '3',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'C99871',
                'color_name' => '206 BUFF BEIGE',
                'image' => '206-buff-beige.jpg',
                'category_color_type_id' => '13',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'DAA578',
                'color_name' => '207 SAND BEIGE',
                'image' => '207-sand-beige.jpg',
                'category_color_type_id' => '7',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'CA9351',
                'color_name' => '209 CARAMEL BEIGE',
                'image' => '209-caramel-beige.jpg',
                'category_color_type_id' => '8',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'Infallible Pro-Glow Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => '974E22',
                'color_name' => '212 COCOA',
                'image' => '212-cocoa.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'INFALLIBLE Up to 24HR Fresh Wear Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'F5D7C3',
                'color_name' => '400 PEARL',
                'image' => '400-pearl.jpg',
                'category_color_type_id' => '1',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'INFALLIBLE Up to 24HR Fresh Wear Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'FCE3D2',
                'color_name' => '405 PORCELAIN',
                'image' => '405-porcelain.jpg',
                'category_color_type_id' => '9',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'INFALLIBLE Up to 24HR Fresh Wear Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'FAD2B8',
                'color_name' => '410 IVORY',
                'image' => '410-ivory.jpg',
                'category_color_type_id' => '10',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'INFALLIBLE Up to 24HR Fresh Wear Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'E6B890',
                'color_name' => '440 Natural ROSE',
                'image' => '440-Natural-rose.jpg',
                'category_color_type_id' => '6',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'INFALLIBLE Up to 24HR Fresh Wear Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'E4B083',
                'color_name' => '445 VANILLA',
                'image' => '445-vanilla.jpg',
                'category_color_type_id' => '7',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],

            [
                'name' => 'INFALLIBLE Up to 24HR Fresh Wear Foundation',
                'category_id' => '3',
                'brand_id' => '2',
                'color_code_hex' => 'DEA468',
                'color_name' => '475 SUN-BEIGE',
                'image' => '475-sun-beige.jpg',
                'category_color_type_id' => '14',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'NARS Velvet Matte Foundation Stick',
                'category_id' => '3',
                'brand_id' => '5',
                'color_code_hex' => 'F4D8B3',
                'color_name' => 'foundation stick siberia',
                'image' => 'foundation_stick_siberia.jpg',
                'category_color_type_id' => '9',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Power Bullet Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => 'B56663',
                'color_name' => 'Natural cool pink',
                'image' => 'natural-cool pink.jpg',
                'category_color_type_id' => '15',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Power Bullet Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => 'D25F5C',
                'color_name' => 'confident peachy nude',
                'image' => 'confident-peachy-nude.jpg',
                'category_color_type_id' => '16',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Power Bullet Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => 'CF395D',
                'color_name' => 'Bachelorette',
                'image' => 'bachelorette.jpg',
                'category_color_type_id' => '19',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Power Bullet Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => 'AE1523',
                'color_name' => 'El Cinco De Mayo',
                'image' => 'el-cinco-de-mayo.jpg',
                'category_color_type_id' => '17',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Liquid Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => 'B56663',
                'color_name' => 'Wild Child',
                'image' => 'wild-child.png',
                'category_color_type_id' => '18',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Liquid Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => 'E45944',
                'color_name' => 'Mamacita',
                'image' => 'mamacita.jpg',
                'category_color_type_id' => '20',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Liquid Matte Lipstick',
                'category_id' => '23',
                'brand_id' => '34',
                'color_code_hex' => '9E273A',
                'color_name' => 'Cheerleader pink',
                'image' => 'cheerleader_pink.png',
                'category_color_type_id' => '21',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'nars Lipstick',
                'category_id' => '23',
                'brand_id' => '5',
                'color_code_hex' => '9E273A',
                'color_name' => 'Orgasm',
                'image' => 'orgasm.jpg',
                'category_color_type_id' => '16',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'nars lip gloss',
                'category_id' => '23',
                'brand_id' => '5',
                'color_code_hex' => 'F2A7AC',
                'color_name' => 'Turkish Delight',
                'image' => 'turkish-delight.jpg',
                'category_color_type_id' => '16',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'E.L.F MOISTURIZING LIPSTICK',
                'category_id' => '23',
                'brand_id' => '16',
                'color_code_hex' => 'CE7358',
                'color_name' => 'Cheeky',
                'image' => 'cheeky.jpg',
                'category_color_type_id' => '16',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'E.L.F lipgloss',
                'category_id' => '23',
                'brand_id' => '16',
                'color_code_hex' => 'CE7358',
                'color_name' => 'raspberry truffle kiss',
                'image' => 'raspberry-truffle-kiss.jpg',
                'category_color_type_id' => '22',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'nyx eyelinear',
                'category_id' => '21',
                'brand_id' => '17',
                'color_code_hex' => '000000',
                'color_name' => 'Bourjois Repack Eyeliner',
                'image' => 'bourjois-repack-eyeliner.jpg',
                'category_color_type_id' => '23',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'nyx eyelinear',
                'category_id' => '28',
                'brand_id' => '17',
                'color_code_hex' => 'ffe9d4',
                'color_name' => 'khol-nude',
                'image' => 'khol-nude.jpg',
                'category_color_type_id' => '24',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'nyx Essence The Smokey Eye Pencil',
                'category_id' => '28',
                'brand_id' => '17',
                'color_code_hex' => '000000',
                'color_name' => 'black',
                'image' => 'black.jpg',
                'category_color_type_id' => '23',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'nyx Lakme Eyeconic Kajal',
                'category_id' => '28',
                'brand_id' => '17',
                'color_code_hex' => '420E0A',
                'color_name' => 'Classic Brown',
                'image' => 'classic-brown.jpg',
                'category_color_type_id' => '7',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'E.L.F Volume pumping mascara',
                'category_id' => '13',
                'brand_id' => '16',
                'color_code_hex' => '000000',
                'color_name' => 'black mascara',
                'image' => 'black-mascara.jpg',
                'category_color_type_id' => '23',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'BD3D47',
                'color_name' => 'Dark pink',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'CC4940',
                'color_name' => 'Pink',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => '954131',
                'color_name' => 'Dark Brown',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'CC8A73',
                'color_name' => 'Light Brown',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'CC6940',
                'color_name' => 'Peach',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'D98A3E',
                'color_name' => 'Peach Yellow',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'DD5F4E',
                'color_name' => 'Light Pink',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Coral Obsessions Eyeshadow Palette',
                'category_id' => '22',
                'brand_id' => '34',
                'color_code_hex' => 'DE6452',
                'color_name' => 'Dark peach',
                'image' => 'coral.png',
                'category_color_type_id' => '26',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Infallible Longwear Blush Shaping Sticks',
                'category_id' => '6',
                'brand_id' => '2',
                'color_code_hex' => 'F58AA8',
                'color_name' => 'sexy flush',
                'image' => 'sexy-flush.jpg',
                'category_color_type_id' => '15',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Anastasia Powder Bronzer',
                'category_id' => '6',
                'brand_id' => '25',
                'color_code_hex' => 'C38063',
                'color_name' => 'rosewood',
                'image' => 'rosewood.jpg',
                'category_color_type_id' => '15',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ],
            [
                'name' => 'Anastasia Powder Bronzer',
                'category_id' => '6',
                'brand_id' => '25',
                'color_code_hex' => 'B27556',
                'color_name' => 'saddle',
                'image' => 'saddle.jpg',
                'category_color_type_id' => '7',
                'created_at' => date("Y-m-d H:i:s"),
                'updated_at' => date("Y-m-d H:i:s")
            ]


        ];
        DB::table('products')->insert($products);
    }
}
