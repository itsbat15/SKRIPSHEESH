<?php

namespace App\Providers;

use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    public function boot(): void
    {
        RateLimiter::for('artha-login', function (Request $request) {
            $email = $request->input('email');
            $identity = is_string($email) ? strtolower(trim($email)) : '';

            return Limit::perMinutes(10, 5)->by($identity.'|'.$request->ip());
        });
    }
}
