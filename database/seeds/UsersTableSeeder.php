<?php

use App\User;
use Illuminate\Database\Seeder;

class UsersTableSeeder extends Seeder
{
    const ADMIN_DOMAIN = 'beauty.com';

    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $admin1 = User::create([
            'name' => 'admin user1',
            'email' => 'admin1@' . self::ADMIN_DOMAIN,
            'password' => Hash::make('admin1'),
        ]);

        $admin1->assignRole('admin');

        $admin2 = User::create([
            'name' => 'admin user2',
            'email' => 'admin2@' . self::ADMIN_DOMAIN,
            'password' => Hash::make('admin2'),
        ]);

        $admin2->assignRole('admin');
    }
}
